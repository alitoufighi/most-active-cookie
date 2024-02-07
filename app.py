from logger import logger
from datetime import date
from exceptions import BadInputException
from cookie_file_parser import CookieFileParser

class MostActiveCookieApp():
    def __init__(self, filename: str):
        self.filename = filename
        self.parsed_cookies = CookieFileParser().parse(filename)
    
    def get_top_used_cookies(self, requested_date: date) -> list:
        if not self.parsed_cookies[requested_date]:
            logger.debug(f'Parsed cookies do not have the date {requested_date}')
            raise BadInputException('This date does not exist in the cookie database')
        # Find `parsed_cookies` with maximum number of occurrences in the `requested_date`
        top_used_cookies = []
        max_value = 0
        for cookie, count in self.parsed_cookies[requested_date].items():
            if count > max_value:
                max_value = count
                top_used_cookies = [cookie]
            elif count == max_value:
                top_used_cookies.append(cookie)
        logger.debug(f'Top used cookies are: {top_used_cookies}')
        return top_used_cookies
