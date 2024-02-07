from logger import logger
from datetime import datetime
from collections import defaultdict
from exceptions import BadInputException

class CookieFileParser():
    @staticmethod
    def parse(filename: str):
        cookie_daily_usages = defaultdict(lambda: defaultdict(int))

        with open(filename) as fp:
            headers = fp.readline().strip().split(',')
            if len(headers) != 2:
                raise BadInputException('Input file should include 2 columns of data')
            try:
                cookie_index = headers.index('cookie')
                timestamp_index = headers.index('timestamp')
            except ValueError:
                raise BadInputException('Column names for input file should include "cookie" and "timestamp".')
            
            for line in fp:
                line = line.strip()
                columns = line.split(',')
                if len(columns) != 2:
                    raise BadInputException('Malformed input file. It should have 2 comma-separated columns for cookie and timestamp.')
                cookie = columns[cookie_index]
                timestamp = columns[timestamp_index]
                logger.debug(f'Read row from csv: cookie={timestamp} timestamp={timestamp}')
                try:
                    usage_date = datetime.fromisoformat(timestamp).date()
                except ValueError:
                    raise BadInputException('Timestamp value is not in ISO format')
                cookie_daily_usages[usage_date][cookie] += 1
        return cookie_daily_usages
