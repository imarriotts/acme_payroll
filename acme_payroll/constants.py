"""
This module contains constant values used throughout the project.
"""
# Data Constants
REGEX_EMPLOYEE = r'^[A-Za-z]+=(?:[A-Z]{2}\d{2}:\d{2}-\d{2}:\d{2},){0,4}[A-Z]{2}\d{2}:\d{2}-\d{2}:\d{2}$'
REGEX_SHIFT = r'([A-Z]{2})(\d{2}:\d{2})-(\d{2}:\d{2})'

# Days Constants
AVAILABLE_DAYS = ("MO", "TU", "WE", "TH", "FR", "SA", "SU")
WEEKDAYS = ("MO", "TU", "WE", "TH", "FR")
DAYS = {
    "MO": "Monday",
    "TU": "Tuesday",
    "WE": "Wednesday",
    "TH": "Thursday",
    "FR": "Friday",
    "SA": "Saturday",
    "SU": "Sunday"
}
WEEKDAY = "weekday"
WEEKEND = "weekend"

# Rates Constants
RATES = {
    'weekday': [
        {'start': '00:01', 'end': '09:00', 'rate': 25},
        {'start': '09:01', 'end': '18:00', 'rate': 15},
        {'start': '18:01', 'end': '00:00', 'rate': 20}
    ],
    'weekend': [
        {'start': '00:01', 'end': '09:00', 'rate': 30},
        {'start': '09:01', 'end': '18:00', 'rate': 20},
        {'start': '18:01', 'end': '23:59', 'rate': 25}
    ]
}

# Messages for errors
INVALID_EMPLOYEE_DATA = "Invalid employee data provided"
INVALID_SHIFT_DATA = "Invalid shift data provided"
INVALID_PAY_RATE = "Pay rate must be greater than zero"
INVALID_HOURS_WORKED = "Hours worked must be greater than zero"
INVALID_SHIFT_TYPE = "Invalid shift type provided"
INVALID_DATE_FORMAT = "Invalid date format provided"
INVALID_DAY_CODE = "Invalid day code provided"
FILE_NOT_FOUND = "File not found"
MISSING_ARGUMENT = "Missing argument for option:"
INVALID_OPTION = "Invalid option:"
RATES_NOT_PROVIDED = "Rates not provided"
INVALID_INPUT = "Invalid input. Please enter a number corresponding to a file in the list."
NO_FILES_FOUND_INPUT = "No .txt files found in input folder. Please add .txt files to the input folder and try again."

# Messages for success
PAYROLL_CALCULATED_SUCCESSFULLY = "Payroll calculated successfully."
PAYROLL_CALCULATED_MESSAGE = "The amount to pay {employee_name} is: {payroll} USD"

# Example data
EXAMPLE_INPUT = "IVAN=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00"
EXAMPLE_OUTPUT = "The amount to pay IVAN is: 85.00 USD"
EXAMPLE_FILE = "acme_payroll/tests/data/employee_data.txt"
EXAMPLE_FILE_COPY = "input/payroll_example.txt"