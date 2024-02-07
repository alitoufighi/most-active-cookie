import logging
from argparse import ArgumentParser
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
    def __init__(self, filename: str, ):
        self.filename = filename
        self.cookie_parser = CookieFileParser(filename)
        self.parsed_cookies = self.cookie_parser.parse()
    
    def get_top_used_cookie(self, desired_date: date):
        if not self.parsed_cookies[desired_date]:
            raise ValueError('This date does not exist in the cookie database')
        # return max(self.parsed_cookies[desired_date], key=self.parsed_cookies[desired_date].get)
        top_used_cookies = []
        max_value = 0
        for cookie, count in self.parsed_cookies[desired_date].items():
            if count > max_value:
                max_value = count
                top_used_cookies = [cookie]
            elif count == max_value:
                top_used_cookies.append(cookie)
        return top_used_cookies
    


if __name__ == '__main__':
    parser = ArgumentParser(description='Finds the most active cookie!')
    parser.add_argument('-f', dest='filename', required=True)
    parser.add_argument('-d', dest='date', required=True, type=date.fromisoformat, help='Asking date in ISO format')
    args = parser.parse_args()
    print(args.filename, args.date)
    
    app = MostActiveCookieApp(args.filename)
    print('\n'.join(app.get_top_used_cookie(args.date)))