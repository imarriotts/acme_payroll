"""
This module contains constant values used throughout the project.
"""

# Days Constants
WEEKDAYS = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday")
WEEKENDS = ("Saturday", "Sunday")
DAYS_CHOICES = WEEKDAYS + WEEKENDS
DAYS_MAP = {
    "MO": "Monday",
    "TU": "Tuesday",
    "WE": "Wednesday",
    "TH": "Thursday",
    "FR": "Friday",
    "SA": "Saturday",
    "SU": "Sunday"
}

# Payroll Constants
SHIFT_MORNING = "Morning Shift"
SHIFT_AFTERNOON = "Afternoon Shift"
SHIFT_NIGHT = "Night Shift"
SHIFT_CHOICES = [SHIFT_MORNING, SHIFT_AFTERNOON, SHIFT_NIGHT]

# Weekday Morning Shift
WEEKDAY_MORNING_START = 1
WEEKDAY_MORNING_END = 9
WEEKDAY_MORNING_PAY = 25

# Weekday Afternoon Shift
WEEKDAY_AFTERNOON_START = 9
WEEKDAY_AFTERNOON_END = 18
WEEKDAY_AFTERNOON_PAY = 15

# Weekday Night Shift
WEEKDAY_NIGHT_START = 18
WEEKDAY_NIGHT_END = 24
WEEKDAY_NIGHT_PAY = 20

# Weekend Morning Shift
WEEKEND_MORNING_START = 1
WEEKEND_MORNING_END = 9
WEEKEND_MORNING_PAY = 30

# Weekend Afternoon Shift
WEEKEND_AFTERNOON_START = 9
WEEKEND_AFTERNOON_END = 18
WEEKEND_AFTERNOON_PAY = 20

# Weekend Night Shift
WEEKEND_NIGHT_START = 18
WEEKEND_NIGHT_END = 24
WEEKEND_NIGHT_PAY = 25

# Messages for errors
INVALID_EMPLOYEE_DATA = "Invalid employee data provided."
INVALID_SHIFT_DATA = "Invalid shift data provided."
INVALID_PAY_RATE = "Pay rate must be greater than zero."
INVALID_HOURS_WORKED = "Hours worked must be greater than zero."
INVALID_SHIFT_TYPE = "Invalid shift type provided."
INVALID_DATE_FORMAT = "Invalid date format provided."

# Messages for success
PAYROLL_CALCULATED_SUCCESSFULLY = "Payroll calculated successfully."