import arg_parser
import unittest
import logging
from unittest.mock import patch
from datetime import date
from exceptions import BadInputException
from arg_parser import ArgumentParser


class TestArgParser(unittest.TestCase):
    """
    Testing argument parsing functions
    """

    def setUp(self):
        logging.disable(logging.CRITICAL)
    
    def tearDown(self):
        logging.disable(logging.NOTSET)


    def test_iso_format_date_with_non_date_input_should_raise_bad_input_exception(self):
        """
        Test that date validation function raises an exception when a non-date input is given or the date is not in ISO format
        """
        self.assertRaises(BadInputException, arg_parser.iso_format_date, 'non-date-input')
        self.assertRaises(BadInputException, arg_parser.iso_format_date, '2018-40-40')
        self.assertRaises(BadInputException, arg_parser.iso_format_date, '2018-20-40')
        self.assertRaises(BadInputException, arg_parser.iso_format_date, '2018-40-20')
        self.assertRaises(BadInputException, arg_parser.iso_format_date, '2018/11/11')

    def test_iso_format_date_with_valid_date_should_return_parsed_date(self):
        """
        Test that date validation function parses a valid input it into a datetime.date object
        """
        self.assertEqual(date(2018, 12, 9), arg_parser.iso_format_date('2018-12-09'))
        self.assertEqual(date(2000, 12, 28), arg_parser.iso_format_date('2000-12-28'))

    def test_accessible_file_with_non_existing_file_should_raise_bad_input_exception(self):
        """
        Test that input file validation function raises an exception when a non-existing or non-accessible file is given
        """
        self.assertRaises(BadInputException, arg_parser.accessible_file, '/tmp')
        self.assertRaises(BadInputException, arg_parser.accessible_file, '/non/existing/path.txt')
    
    def test_argument_parser_read_args_with_no_args_should_exit_with_non_zero_code(self):
        """
        Test that the argument parser will exit the program with non-zero code if the required arguments are not properly set
        """
        with patch('argparse._sys.argv', ['python', 'main.py']):
            with self.assertRaises(SystemExit) as cm:
                ArgumentParser.read_args()
            self.assertNotEqual(cm.exception.code, 0)

        with patch('argparse._sys.argv', ['python', 'main.py', '-f', 'input.txt']):
            with self.assertRaises(SystemExit) as cm:
                ArgumentParser.read_args()
            self.assertNotEqual(cm.exception.code, 0)

        with patch('argparse._sys.argv', ['python', 'main.py', '-d', '2018-12-09']):
            with self.assertRaises(SystemExit) as cm:
                ArgumentParser.read_args()
            self.assertNotEqual(cm.exception.code, 0)

