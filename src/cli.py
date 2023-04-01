

from typing import List
from .constants import RATES

from .payroll.payroll import PayrollService
from .shift.shift import Shift
from .employee.employee_io import EmployeeIO
from .employee.employee_service import EmployeeService


def manualProcessing(args: list[str]):
    options = {'-h': printHelp, '-a': printAbout,
               '-f': processFile, '-i': processInput}
    for i in range(len(args)):
        if args[i] in options:
            if args[i] in ['-f', '-i']:
                if i+1 < len(args):
                    options[args[i]](args[i + 1])
                else:
                    print(f"Missing argument for option {args[i]}")
                    exit(1)
            else:
                options[args[i]]()
        else:
            print('Invalid option: ' + args[i])
            exit(1)


def processFile(file: str):
    print('Processing file: ' + file)
    employee_io = EmployeeIO(file)
    employee_service = EmployeeService(shift_class=Shift)
    employee_data, validation_errors = employee_io.read_employee_data()
    checkForErrors(file, validation_errors)
    employees = employee_service.create_employee_list(employee_data)

    # Build the PayrollService object
    payroll_service = PayrollService.Builder(employees=employees).with_rates(RATES).build()

    # Calculate the payroll
    employeesPayroll = payroll_service.calculate_payroll()

    for payroll in employeesPayroll:
        print(payroll)
        
    exit(1)


def processInput(input: str):
    print('processinput')
    exit(1)


def automaticProcessing():
    print('automaticProcessing')


def printHelp():
    print('Help')
    exit(1)


def printAbout():
    print('About')
    exit(1)


def checkForErrors(file: str, validation_errors: List[str]):
    if len(validation_errors) > 0:
        print('They are some errors in the file:')
        for error in validation_errors:
            print(error)
        print('\nPlease fix them and try again')
        print('Would you like to try again? (y/n)')
        answer = input()
        if answer == 'y':
            processFile(file)
        exit(1)
