import os
import shutil
import unittest
from unittest.mock import patch

from io import StringIO

from acme_payroll.cli import automatic_processing, manual_processing, print_about, print_help, check_for_errors, process_file, process_input
from acme_payroll.constants import EXAMPLE_FILE, EXAMPLE_INPUT, EXAMPLE_OUTPUT


class TestCli(unittest.TestCase):

    @patch('sys.stdout', new_callable=StringIO)
    def test_print_help(self, mock_stdout):
        with self.assertRaises(SystemExit) as cm:
            print_help()
        self.assertEqual(cm.exception.code, 1)
        expected_output = 'Help: ACME Payroll System\n\nUsage: python acme_payroll.py [options]\n\nOptions:\n\n-h, --help \t\t\t\t\t Display this help message\n-a, --about \t\t\t\t\t Display information about the ACME Payroll System\n-f <filename>, --file <filename> \t\t Process payroll from a given file\n-i <input_string>, --input <input_string> \t Process payroll from a given input string\nWithout any options\t\t\t\t The program will run in automatic mode'
        self.assertEqual(mock_stdout.getvalue().strip(), expected_output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_check_for_errors_file(self, mock_stdout):
        with patch('builtins.input', return_value='n'):
            with self.assertRaises(SystemExit) as cm:
                check_for_errors('file context', ['Error 1', 'Error 2'])
        self.assertEqual(cm.exception.code, 1)

        expected_output = 'They are some errors in the file:\n\nError 1\nError 2\n\nPlease fix them and try again\nWould you like to try again? (y/n)'
        self.assertEqual(mock_stdout.getvalue().strip(), expected_output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_check_for_errors_input(self, mock_stdout):
        with self.assertRaises(SystemExit) as cm:
            check_for_errors('input context', ['Error 1'], is_input=True)
        self.assertEqual(cm.exception.code, 1)

        expected_output = 'They is an error in the input:\n\nError 1\n\nPlease fix it and try again'
        self.assertEqual(mock_stdout.getvalue().strip(), expected_output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_print_about(self, mock_stdout):
        with self.assertRaises(SystemExit) as cm:
            print_about()
        self.assertEqual(cm.exception.code, 1)
        expected_output = 'ACME Payroll System v1.0\nDeveloped by Ivan M.\nCopyright © 2023'
        self.assertEqual(mock_stdout.getvalue().strip(), expected_output)

    def test_automatic_processing(self):
        expected_output = 'Please select a file to process:\n\t1. test_example.txt\nThe amount to pay IVAN is: 85.00 USD'
        # Create input folder and example file
        if not os.path.exists('input'):
            os.makedirs('input')
        with open('input/test_example.txt', 'w') as f:
            f.write(EXAMPLE_INPUT)
        # if there is any other file in the folder, move it to a temp folder to avoid errors in the test
        if len(os.listdir('input')) > 1:
            if not os.path.exists('input/temp'):
                os.makedirs('input/temp')
            for file in os.listdir('input'):
                if file != 'test_example.txt':
                    shutil.move(f'input/{file}', 'input/temp')
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            with patch('builtins.input', return_value=1):
                with self.assertRaises(SystemExit) as cm:
                    # Call automatic_processing()
                    automatic_processing()
                    # Remove input file if exists
                    self.assertEqual(cm.exception.code, 1)
        # Check that the captured output matches the expected output
        self.assertEqual(
            mock_stdout.getvalue().strip(), expected_output)
        # Remove input file if exists
        if os.path.exists('input/test_example.txt'):
            os.remove('input/test_example.txt')
        # Remove input folder if empty
        if os.path.exists('input') and not os.listdir('input'):
            shutil.rmtree('input')
        # Move files from temp folder to input folder
        if os.path.exists('input/temp'):
            for file in os.listdir('input/temp'):
                shutil.move(f'input/temp/{file}', 'input')
            shutil.rmtree('input/temp')

    def test_manual_processing(self):
        # Test case for valid command line arguments
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            with self.assertRaises(SystemExit) as cm:
                manual_processing(['-a'])
            self.assertEqual(cm.exception.code, 1)
            expected_output = 'ACME Payroll System v1.0\nDeveloped by Ivan M.\nCopyright © 2023'
            self.assertEqual(mock_stdout.getvalue().strip(), expected_output)

        # Test case for invalid option
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            with self.assertRaises(SystemExit) as cm:
                manual_processing(['-x'])
            self.assertEqual(cm.exception.code, 1)
            expected_output = 'Invalid option: -x'
            self.assertEqual(mock_stdout.getvalue().strip(), expected_output)

        # Test case for missing argument
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            with self.assertRaises(SystemExit) as cm:
                manual_processing(['-f'])
            self.assertEqual(cm.exception.code, 1)
            expected_output = 'Missing argument for option: -f'
            self.assertEqual(mock_stdout.getvalue().strip(), expected_output)

    def test_process_file(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            with self.assertRaises(SystemExit) as cm:
                process_file(EXAMPLE_FILE)
                expected_output = 'The amount to pay IVAN is: 85.00 USD'
                self.assertEqual(
                    mock_stdout.getvalue().strip(), expected_output)
            self.assertEqual(cm.exception.code, 1)

    def test_process_wrong_file(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            with self.assertRaises(SystemExit) as cm:
                process_file('some_wrong_file.txt')
                full_path = os.path.abspath('some_wrong_file.txt')
                expected_output = 'ERROR:root:File not found: ' + full_path
                print(mock_stdout.getvalue().strip(),   expected_output)
                self.assertEqual(
                    mock_stdout.getvalue().strip(), expected_output)
            self.assertEqual(cm.exception.code, 1)

    def test_process_input(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            with self.assertRaises(SystemExit) as cm:
                process_input(EXAMPLE_INPUT)
                self.assertEqual(mock_stdout.getvalue(), EXAMPLE_OUTPUT)
            self.assertEqual(cm.exception.code, 1)

if __name__ == '__main__':
    unittest.main()
