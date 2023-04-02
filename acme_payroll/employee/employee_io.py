from typing import List, Tuple

from acme_payroll.exceptions import FileException

from acme_payroll.utils.utils import Utils

class EmployeeIO:
    """
    A class that handles input/output operations related to employee data.
    """

    def __init__(self, file_path: str):
        self.file_path = Utils.get_file_path(file_path)

    def read_employee_data(self) -> Tuple[List[str], List[str]]:
        """
        Reads employee data from a file and validates it.
        Returns a tuple containing the employee data and any validation errors encountered.
        """
        # checks if file exists
        if not Utils.file_exists(self.file_path):
            raise FileException(file_path = self.file_path)
        employee_data = []
        validation_errors = []
        with open(self.file_path, 'r') as f:
            employee_data = [line.strip() for line in f.readlines()]
        validation_errors = Utils.validate_employee_data(employee_data)
        return employee_data, validation_errors
