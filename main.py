import logging
from datetime import date, datetime
from collections import defaultdict

class CookieFileParser():
    def __init__(self, filename: str):
        self.filename = filename
        self.cookie_daily_usages = defaultdict(lambda: defaultdict(int))

    def parse(self):
        with open(self.filename) as fp:
            headers = fp.readline().strip().split(',')
            if len(headers) != 2:
                raise ValueError('Input file should include 2 columns of data')
                # exit(-1)
            try:
                cookie_index = headers.index('cookie')
                timestamp_index = headers.index('timestamp')
            except ValueError:
                raise ValueError('Column names for input file should include "cookie" and "timestamp".')
                # exit(-1)
            
            for line in fp:
                line = line.strip()
                columns = line.split(',')
                cookie = columns[cookie_index]
                timestamp = columns[timestamp_index]
                usage_date = datetime.fromisoformat(timestamp).date()
                self.cookie_daily_usages[usage_date][cookie] += 1
        return self.cookie_daily_usages


class MostActiveCookieApp():
    def __init__(self, filename: str, desired_date: date):
        self.filename = filename
        self.desired_date = desired_date
        self.cookie_parser = CookieFileParser(filename)
        self.parsed_cookies = self.cookie_parser.parse()
    
    def get_top_used_cookie(self):
        if not self.parsed_cookies[self.desired_date]:
            raise ValueError('This date does not exist in the cookie database')
        return max(self.parsed_cookies[self.desired_date], key=self.parsed_cookies[self.desired_date].get)
    


if __name__ == '__main__':
    app = MostActiveCookieApp('input.txt', date.fromisoformat('2018-12-09'))
    print(app.get_top_used_cookie())