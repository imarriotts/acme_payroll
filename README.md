# A CLI Payroll Calculator for the ACME Company

## Project Structure
- `acme_payroll.py`: This is a Python module that contains code for the main entry point of the application. It can be executed to start the payroll system or may be imported as a module by other scripts or modules.

- `README.md`: This is a text file at the root level of the project, which contains documentation or instructions for the project.

- `.gitignore`: This is a configuration file at the root level of the project, which tells Git which files and directories to ignore when committing changes to the repository.

- `src`: This is a directory that contains the main source code for the project.

- `constants.py`: This is a Python module that contains constant values used throughout the project.

- `exceptions.py`: This is a Python module that defines custom exceptions classes or functions for handling exceptions within the project.

- `payroll`: This is a directory that contains the source code for payroll-related functionality.

    - `payroll_service.py`: This is a Python module that provides a service for calculating payroll.

    - `payroll.py`: This is a Python module that defines classes and functions related to payroll calculations.

    - `__init__.py`: This is a Python module that marks the `payroll` directory as a Python package.

- `employee`: This is a directory that contains the source code for managing employee data.

    - `employee.py`: This is a Python module that defines classes and functions related to employees.

    - `employee_io.py`: This is a Python module that provides functions for reading and writing employee data to a file or database.

    - `employee_service.py`: This is a Python module that provides a service for managing employees.

    - `__init__.py`: This is a Python module that marks the `employee` directory as a Python package.

- `utils`: This is a directory that contains utility functions used throughout the project.

    - `utils.py`: This is a Python module that defines utility functions for general use.

    - `__init__.py`: This is a Python module that marks the `utils` directory as a Python package.

- `shift`: This is a directory that contains the source code for managing work shifts.

    - `shift.py`: This is a Python module that defines classes and functions related to work shifts.

    - `shift_service.py`: This is a Python module that provides a service for managing work shifts.

    - `__init__.py`: This is a Python module that marks the `shift` directory as a Python package.

- `tests`: This is a directory that contains the unit tests for the project.

    - `test_payroll.py`: This is a Python module that contains unit tests for the `payroll` module.

    - `test_payroll_service.py`: This is a Python module that contains unit tests for the `payroll_service` module.

    - `test_employee.py`: This is a Python module that contains unit tests for the `employee` module.

    - `test_employee_io.py`: This is a Python module that contains unit tests for the `employee_io` module.

    - `test_employee_service.py`: This is a Python module that contains unit tests for the `employee_service` module.

    - `test_utils.py`: This is a Python module that contains unit tests for the `utils` module.

    - `test_shift.py`: This is a Python module that contains unit tests for the `shift` module.

    - `test_shift_service.py`: This is a Python module that contains unit tests for the `shift_service` module.

    - `__init__.py`: This is a Python module that marks each of the `
