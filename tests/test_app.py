import unittest
import logging
from unittest.mock import patch, mock_open
from datetime import date
from exceptions import BadInputException
from app import MostActiveCookieApp

class TestMostActiveCookieApp(unittest.TestCase):
    """
    Testing application level functionalities
    """

    def setUp(self):
        logging.disable(logging.CRITICAL)
    
    def tearDown(self):
        logging.disable(logging.NOTSET)


    def test_get_top_used_cookies_with_a_date_not_existing_in_database_will_raise_bad_input_exception(self):
        """
        Test that given a non existent date in the database the app will raise BadInputException
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
        with patch("builtins.open", mock_open(read_data=file_contents)):
            app = MostActiveCookieApp('/tmp/input.csv')
            self.assertRaises(BadInputException, app.get_top_used_cookies, date(2015, 11, 10))
    
    def test_get_top_used_cookies_with_single_top_result_should_return_a_list_including_only_the_single_top_item(self):
        """
        Test that if there is only a single top cookie in a given day, only that one will be returned in a list
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
        with patch("builtins.open", mock_open(read_data=file_contents)):
            app = MostActiveCookieApp('/tmp/input.csv')
            self.assertEqual(['4sMM2LxV07bPJzwf'], app.get_top_used_cookies(date(2018, 12, 7)))
    
        with patch("builtins.open", mock_open(read_data=file_contents)):
            app = MostActiveCookieApp('/tmp/input.csv')
            self.assertEqual(['AtY0laUfhglK3lC7'], app.get_top_used_cookies(date(2018, 12, 9)))
    

    def test_get_top_used_cookies_with_multiple_top_result_should_return_a_list_with_all_of_top_items(self):
        """
        Test that if there are multiple top cookies in a given day, all of them will be returned in a list
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
        with patch("builtins.open", mock_open(read_data=file_contents)):
            app = MostActiveCookieApp('/tmp/input.csv')
            self.assertEqual(['SAZuXPGUrfbcn5UA', '4sMM2LxV07bPJzwf', 'fbcn5UAVanZf6UtG'], app.get_top_used_cookies(date(2018, 12, 8)))
    