
import os
import shutil
from typing import List

from acme_payroll.constants import EXAMPLE_FILE, EXAMPLE_FILE_COPY, INVALID_INPUT, MISSING_ARGUMENT, NO_FILES_FOUND_INPUT, RATES, INVALID_OPTION
from acme_payroll.payroll.payroll import PayrollService
from acme_payroll.shift.shift import Shift
from acme_payroll.employee.employee_io import EmployeeIO, EmployeeInputSingle
from acme_payroll.employee.employee_service import EmployeeService


def manual_processing(args: list[str]):
    """
    Process the command line arguments and call the appropriate function.

    Args:
        args (list[str]): The list of command line arguments.

    Returns:
        None
    """
    options = {'-h': print_help, '-a': print_about,
               '-f': process_file, '-i': process_input}
    for i in range(len(args)):
        if args[i] in options:
            if args[i] in ['-f', '-i']:
                if i+1 < len(args):
                    options[args[i]](args[i + 1])
                else:
                    print(f"{MISSING_ARGUMENT} {args[i]}")
                    exit(1)
            else:
                options[args[i]]()
        else:
            print(f"{INVALID_OPTION} {args[i]}")
            exit(1)


def process_file(file: str):
    """Process employee data from a file and calculate the payroll.

    :param file: A string representing the path to the file containing employee data.
    """

    # Build the EmployeeIO object
    employee_io = EmployeeIO(file)

    # Build the EmployeeService object
    employee_service = EmployeeService(shift_class=Shift)

    #  Read the employee data
    employee_data, validation_errors = employee_io.read_employee_data()

    # Check for errors
    check_for_errors(file, validation_errors)

    # Create the employee list
    employees = employee_service.create_employee_list(employee_data)

    # Build the PayrollService object
    payroll_service = PayrollService.Builder(
        employees=employees).with_rates(RATES).build()

    # Calculate the payroll
    employeesPayroll = payroll_service.calculate_payroll()

    # Print the payroll
    for payroll in employeesPayroll:
        print(payroll)

    # exit
    exit(1)


def process_input(input: str):
    """
    Process employee data from a string and calculate the payroll.

    :param input: A string representing raw input to be processed.
    """
    # Build the EmployeeIO object
    employee_input = EmployeeInputSingle(input)

    # Build the EmployeeService object
    employee_service = EmployeeService(shift_class=Shift)

    #  Read the employee data
    employee_data, validation_errors = employee_input.parse_employee_data()

    # Check for errors
    check_for_errors(input, validation_errors, True)

    # Create the employee list
    employees = employee_service.create_employee_list(employee_data)

    # Build the PayrollService object
    payroll_service = PayrollService.Builder(
        employees=employees).with_rates(RATES).build()

    # Calculate the payroll
    employeesPayroll = payroll_service.calculate_payroll()

    # Print the payroll
    for payroll in employeesPayroll:
        print(payroll)

    exit(1)


def automatic_processing():
    """
    Automatically process a file from the input folder and calculate the payroll.
    """
    # Create input folder if it doesn't exist
    if not os.path.exists('input'):
        os.makedirs('input')
        # Copy example file to input folder
        shutil.copy2(EXAMPLE_FILE, EXAMPLE_FILE_COPY)
        print("A folder named 'input' has been created in the current directory.")
        print("It contains an example file named 'payroll_example.txt'.")
        print("If you would like to process a different file, please add it to the input folder and try again.")

    # Get list of txt files in input folder
    txt_files = [f for f in os.listdir('input') if f.endswith('.txt')]

    # If no txt files found, prompt user to add files to input folder
    if not txt_files:
        print(NO_FILES_FOUND_INPUT)
        return
    # if there is a file called test_example.txt only show that file, this is for testing purposes
    txt_files = [f for f in txt_files if f == 'test_example.txt'] if 'test_example.txt' in txt_files else txt_files

    # Print list of available files for user to select
    print("Please select a file to process:")
    for i, file in enumerate(txt_files):
        print(f"\t{i+1}. {file}")

    # Prompt user to select a file to process
    while True:
        try:
            choice = int(input("\nEnter a number to select a file: "))
            if choice not in range(1, len(txt_files)+1):
                raise ValueError
            break
        except ValueError:
            print(INVALID_INPUT)
            automatic_processing()

    # Process selected file
    file = txt_files[choice-1]
    try:
        process_file(f"input/{file}")
    except Exception as e:
        # Print error and prompt user to try again
        print(f"Error processing file '{file}': {e}")
        choice = input("Would you like to try again? (y/n): ")
        if choice.lower() == 'y':
            process_file(f"input/{file}")
        else:
            print("Exiting program.")
            exit(1)


def print_help():
    """
    Displays help message to show available command line options.
    """
    print('Help: ACME Payroll System\n')
    print('Usage: python acme_payroll.py [options]\n')
    print('Options:\n')
    print('-h, --help \t\t\t\t\t Display this help message')
    print('-a, --about \t\t\t\t\t Display information about the ACME Payroll System')
    print('-f <filename>, --file <filename> \t\t Process payroll from a given file')
    print('-i <input_string>, --input <input_string> \t Process payroll from a given input string')
    print('Without any options\t\t\t\t The program will run in automatic mode')
    exit(1)


def print_about():
    """
    Prints the about message to show in console
    """
    print('ACME Payroll System v1.0\nDeveloped by Ivan M.\nCopyright © 2023')
    exit(1)


def check_for_errors(context_str: str, validation_errors: List[str], is_input: bool = False):
    """
    Check for errors in the file and prompt the user to try again.
    """
    if len(validation_errors) > 0:
        if not is_input:
            print('They are some errors in the file:\n')
            for error in validation_errors:
                print(error)
            print('\nPlease fix them and try again')
            print('Would you like to try again? (y/n)')
            answer = input()
            if answer == 'y':
                process_file(context_str)
        else:
            print('They is an error in the input:\n')
            for error in validation_errors:
                print(error)
            print('\nPlease fix it and try again')

        exit(1)
