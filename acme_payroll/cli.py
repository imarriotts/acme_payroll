

from typing import List

from acme_payroll.constants import MISSING_ARGUMENT, RATES, INVALID_OPTION
from acme_payroll.payroll.payroll import PayrollService
from acme_payroll.shift.shift import Shift
from acme_payroll.employee.employee_io import EmployeeIO
from acme_payroll.employee.employee_service import EmployeeService


def manual_processing(args: list[str]):
    """
    Process the command line arguments and call the appropriate function.

    Args:
        args (list[str]): The list of command line arguments.

    Returns:
        None
    """
    options = {'-h': print_help, '-a': print_about, '-f': process_file, '-i': process_input}
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
    print('Processing file: ' + file)

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
    payroll_service = PayrollService.Builder(employees=employees).with_rates(RATES).build()
    
    # Calculate the payroll
    employeesPayroll = payroll_service.calculate_payroll()
    
    # Print the payroll 
    for payroll in employeesPayroll:
        print(payroll)
    
    # exit
    exit(1)


def process_input(input: str):
    print('process_input')
    exit(1)


def automatic_processing():
    print('automatic_processing')


def print_help():
    """Displays help message to show available command line options."""
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
    """Prints the about message to show in console"""
    print('ACME Payroll System v1.0\nDeveloped by Ivan M.\nCopyright © 2023')
    exit(1) 


def check_for_errors(file: str, validation_errors: List[str]):
    if len(validation_errors) > 0:
        print('They are some errors in the file:')
        for error in validation_errors:
            print(error)
        print('\nPlease fix them and try again')
        print('Would you like to try again? (y/n)')
        answer = input()
        if answer == 'y':
            process_file(file)
        exit(1)
