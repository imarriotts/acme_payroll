import unittest
from unittest.mock import patch

from acme_payroll.cli import manual_processing


class TestManualProcessing(unittest.TestCase):
    
    @patch('acme_payroll.cli.process_file')
    def test_process_file_option(self, mock_process_file):
        with self.assertRaises(SystemExit) as cm, patch('builtins.print'):
            manual_processing(['-f', 'some_file.txt'])
            mock_process_file.assert_called_once_with('some_file.txt')
        self.assertEqual(cm.exception.code, 1)

    @patch('acme_payroll.cli.process_input')
    def test_process_input_option(self, mock_process_input):
        with self.assertRaises(SystemExit) as cm, patch('builtins.print'):
            manual_processing(['-i', 'some_data'])
            mock_process_input.assert_called_once_with('some_data')
        self.assertEqual(cm.exception.code, 1)
        
    @patch('acme_payroll.cli.print_help')
    def test_print_help_option(self, mock_print_help):
        with patch('builtins.print'):
            manual_processing(['-h'])
            mock_print_help.assert_called_once()

    @patch('acme_payroll.cli.print_about')
    def test_print_about_option(self, mock_print_about):
        with patch('builtins.print'):
            manual_processing(['-a'])
            mock_print_about.assert_called_once()

    def test_invalid_option(self):
        with self.assertRaises(SystemExit) as cm, patch('builtins.print'):
            manual_processing(['-x'])
        self.assertEqual(cm.exception.code, 1)

    def test_missing_argument(self):
        with self.assertRaises(SystemExit) as cm, patch('builtins.print'):
            manual_processing(['-f'])
        self.assertEqual(cm.exception.code, 1)


if __name__ == '__main__':
    unittest.main()
