import unittest
import logging
from unittest.mock import patch, mock_open
from datetime import date
from exceptions import BadInputException
from cookie_file_parser import CookieFileParser

class TestCookieFileParser(unittest.TestCase):
    """
    Testing cookie file parsing
    """

    def setUp(self):
        logging.disable(logging.CRITICAL)
    
    def tearDown(self):
        logging.disable(logging.NOTSET)


    def test_parse_with_more_or_less_than_2_columns_will_raise_bad_input_exception(self):
        """
        Test that parsing a cookie file that has less or more than 2 columns will raise BadInputException
        """

        file_contents = """cookie,timestamp,peanuts
1234,now,2
"""
        with patch("builtins.open", mock_open(read_data=file_contents)) as mock_file:
            self.assertRaises(BadInputException, CookieFileParser.parse, '/tmp/input.csv')
        mock_file.assert_called_with('/tmp/input.csv')
        ####
        file_contents = """peanuts
1234
123
"""
        with patch("builtins.open", mock_open(read_data=file_contents)):
            self.assertRaises(BadInputException, CookieFileParser.parse, '/tmp/input.csv')
        ####
        file_contents = """cookie,timestamp
1234,not-iso-format
"""
        with patch("builtins.open", mock_open(read_data=file_contents)):
            self.assertRaises(BadInputException, CookieFileParser.parse, '/tmp/input.csv')
        ####
        file_contents = """cookie,timestamp
1234,not-iso-format
"""
        with patch("builtins.open", mock_open(read_data=file_contents)):
            self.assertRaises(BadInputException, CookieFileParser.parse, '/tmp/input.csv')
    
    def test_parse_with_correct_input_format_will_parse_and_return_cookie_daily_usages(self):
        """
        Test that parsing a cookie file that has the correct format will return the parsed daily usages of cookies
        """

        file_contents = """cookie,timestamp
AtY0laUfhglK3lC7,2018-12-09T14:19:00+00:00
SAZuXPGUrfbcn5UA,2018-12-09T10:13:00+00:00
5UAVanZf6UtGyKVS,2018-12-09T07:25:00+00:00
AtY0laUfhglK3lC7,2018-12-09T06:19:00+00:00
SAZuXPGUrfbcn5UA,2018-12-08T22:03:00+00:00
4sMM2LxV07bPJzwf,2018-12-08T21:30:00+00:00
fbcn5UAVanZf6UtG,2018-12-08T09:30:00+00:00
4sMM2LxV07bPJzwf,2018-12-07T23:30:00+00:00
"""

        expected_output = {
            date(2018, 12, 9): {'AtY0laUfhglK3lC7': 2, 'SAZuXPGUrfbcn5UA': 1, '5UAVanZf6UtGyKVS': 1},
            date(2018, 12, 8): {'SAZuXPGUrfbcn5UA': 1, '4sMM2LxV07bPJzwf': 1, 'fbcn5UAVanZf6UtG': 1},
            date(2018, 12, 7): {'4sMM2LxV07bPJzwf': 1}
        }
        with patch("builtins.open", mock_open(read_data=file_contents)):
            self.assertEqual(expected_output, CookieFileParser.parse('/tmp/input.csv'))
    