# ACME Payroll System

## Overview
ACME Payroll is a payroll processing application that allows employers to calculate the pay of their employees based on their hours worked and hourly rate. The application can process employee data from a file or from user input, and can output the results to the console. It also includes a help menu and an about page.

-----------------------
## Architecture

The ACME Payroll System is built using Python 3.10 and follows a modular architecture pattern. The application is built using the command line interface (CLI) pattern, which allows for easy integration with other applications.

The system uses object-oriented programming (OOP) principles extensively to encapsulate functionality and reduce code duplication. Each class is responsible for a specific task and is designed to be easily testable.

The application is thoroughly tested using the unittest framework. There are tests for each module, including tests for edge cases and error handling. The tests are automated using GitHub Actions, which runs the tests on every commit and pull request.

### Project Structure

This project has a well-organized file structure to make it easy to navigate and maintain. The main directory contains the `acme_payroll.py` file, which serves as the entry point to the application. Additionally, the `constants.py` file contains constants that are used throughout the project. 

The `acme_payroll` directory contains the main application code, including subdirectories for `employee`, `payroll`, `shift`, and `utils`, which contain the respective classes and functions for each domain. The `tests` directory contains unit tests for the various modules in the project. 

Finally, the `.vscode` and `.github` directories contain configurations for the Visual Studio Code editor and GitHub workflows, respectively. 

Here's a visual representation of the project structure:

    |-.vscode
    | |-launch.json
    |-acme_payroll
    | |-constants.py
    | |-cli.py
    | |-payroll
    | | |-payroll.py
    | | |-__init__.py
    | |-employee
    | | |-employee.py
    | | |-employee_io.py
    | | |-employee_service.py
    | | |-__init__.py
    | |-utils
    | | |-utils.py
    | | |-__init__.py
    | |-__init__.py
    | |-exceptions.py
    | |-shift
    | | |-shift.py
    | | |-__init__.py
    | |-tests
    | | |-data
    | | | |-employee_data.txt
    | | |-payroll
    | | | |-test_payroll.py
    | | | |-__init__.py
    | | |-employee
    | | | |-test_employee_io.py
    | | | |-test_employee.py
    | | | |-test_employee_service.py
    | | | |-__init__.py
    | | |-utils
    | | | |-test_utils.py
    | | | |-__init__.py
    | | |-__init__.py
    | | |-shift
    | | | |-test_shift.py
    | | | |-__init__.py
    | | |-test_cli.py
    |-.github
    | |-workflows
    | | |-test.yml
    |-acme_payroll.py
    |-README.md
    |-.gitignore
    |-LICENSE

The main modules are as follows:

- `acme_payroll.py`: The main entry point for the project.
- `constants.py`: Contains constants used in the project, such as rates.
- `cli.py`: Contains the command line interface code for the project.
- `exceptions.py`: Contains custom exception classes used in the project.
- `payroll`: A package containing the code related to calculating payroll for employees.
    - `payroll.py`: Contains the PayrollService class responsible for calculating payroll for employees.
- `employee`: A package containing the code related to managing employee data.
    - `employee.py`: Contains the Employee class for representing an employee and their shifts.
    - `employee_io.py`: Contains the EmployeeIO class for reading employee data from a file.
    - `employee_service.py`: Contains the EmployeeService class for creating employee objects from employee data.
- `shift`: A package containing the code related to managing employee shifts.
    - `shift.py`: Contains the Shift class for representing a shift worked by an employee.
- `utils`: A package containing utility functions used throughout the project.
    - `utils.py`: Contains utility functions used throughout the project.
- `tests`: Contains the test cases for the project.
    - `data`: Contains the input files for the test cases.
    - `payroll`: Contains test cases for the payroll module.
    - `employee`: Contains test cases for the employee module.
    - `shift`: Contains test cases for the shift module.
    - `utils`: Contains test cases for the utils module.
    - `test_cli.py`: Contains test cases for the command line interface.

Finally, the project includes a suite of unit tests to ensure the correctness of the application's behavior. The tests are implemented using the built-in unittest module in Python, and are located in the `acme_payroll/tests` directory. 

The test cases cover all the major functionalities of the application, including employee management, shifts and payroll generation. The tests are automatically executed on push and pull request events using GitHub Actions.

### Design Patterns Used

- Service Layer Pattern: Service classes encapsulate the application's domain logic and expose it through a simple, unified interface. The service class used in this solution is `EmployeeService`.

- Repository Pattern: While this solution doesn't have a traditional database or data store, the use of the `EmployeeIO` class can be seen as performing a similar function as a repository. It provides a standardized way to read employee data from a file, encapsulating the logic for accessing and parsing the data. Similarly, the `Shift` class provides a standardized way to parse shift data from a string. Together, they perform a similar function as repositories in providing a standardized way to access and parse data.

- Command Line Interface Pattern: The command line interface pattern provides a simple, interactive interface to the application's functionality. This pattern is implemented in cli.py.

- Dependency Injection: The EmployeeService class depends on the Shift class, which is injected as a dependency through the constructor. This allows for easier testing and decouples the EmployeeService class from the Shift class implementation.

- Builder: The PayrollService class is built using the Builder pattern, allowing for a more flexible and configurable way of creating objects.

-----------------------
## Approach and Methodology

The application was developed using test-driven development (TDD) principles, with automated unit tests for each module and integration tests for the entire application. 
The tests were run automatically using a continuous integration (CI) system through Github workflows to ensure that the application was functioning correctly at all times.
Additionally, Github projects were used to keep track of the tasks and progress throughout the development process. ACME Payroll was developed using an agile methodology, with frequent feedback and iteration throughout the development process.
The project was managed using a version control system (Git) and hosted on a remote repository (GitHub) for collaboration and backup.

-----------------------
## Local Setup

To run the ACME Payroll System locally, you'll need Python 3.10 installed. Follow these steps:

- Depending on your operating system, you may need to use `python3` instead of `python`
### Clone the repository: 
 ```bash
 git clone https://github.com/imarriotts/acme_payroll
 ```
### Navigate to the project directory:
 ```bash 
cd acme-payroll
```
### Manual Processing of Input File:
-   For a sample input file, see `acme_payroll/tests/data/employee_data.txt`
 ```bash
python acme_payroll.py -f employee_data.txt
```
-   The `-f` flag is used to specify the input file containing employee data.
-   The `filename.txt` argument is the name of the input file containing employee data.

### Run the CLI with the `-h` or `-a` flags for more information:
 ```bash
python acme_payroll.py -h
python acme_payroll.py -a
```
-   The `-h` flag displays the help message for the CLI.
-   The `-a` flag displays the about message for the CLI.
### Automatic Processing of Input File:
 ```bash
python acme_payroll.py
```
-   If no input file is specified, the CLI will automatically read a directory of input, and ask the user to select a file to process.

### Single Line Input Processing:
 ```bash
python acme_payroll.py -i "IVAN=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00"
```
-   The `-i` flag is used to specify a single line of employee data.
-   The `IVAN=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00` argument is a single line of employee data.
-  The CLI will automatically process the input and display the output.
-----------------------
## Testing

The ACME Payroll System includes a suite of unit tests to ensure code quality and prevent regressions. To run the tests locally, follow these steps:

Navigate to the project directory: 
```bash
cd acme-payroll
```
Run the tests: 
```bash
python -m unittest discover -s acme_payroll/tests
```
-----------------------
## Afterword

The ACME Payroll System was a challenging and rewarding project to work on. By utilizing design patterns, test-driven development, and agile methodologies, I was able to create a robust and maintainable application. Additionally, leveraging the power of Git and GitHub allowed for seamless collaboration and version control, while GitHub Actions simplified the testing and deployment process. I am proud of the final product and excited to see how it may be used to streamline payroll processing for businesses.

-----------------------
## License

This project is licensed under the GNU GENERAL PUBLIC LICENSE - see the [LICENSE](LICENSE) file for details.
