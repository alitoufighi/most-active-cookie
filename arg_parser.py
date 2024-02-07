import os
import argparse
from logger import logger
from os.path import isfile, exists
from datetime import date
from exceptions import BadInputException

# Validate whether the input file exists and the user has read access to it
def accessible_file(filename):
    logger.debug(f'Passed filename={filename}')
    if not exists(filename) or not isfile(filename):
        logger.debug(f'Input file does not exist')
        raise BadInputException("Input file does not exist in the provided path")
    if not os.access(filename, os.R_OK):
        logger.debug(f'Input file is not accessible')
        raise BadInputException("Cannnt read a file from the provided path")
    return filename

# Validate whether the input date is in the ISO format
def iso_format_date(date_str):
    logger.debug(f'Passed date string={date_str}')
    try:
        iso_date = date.fromisoformat(date_str)
    except ValueError as e:
        raise BadInputException(e)
    return iso_date

class ArgumentParser():
    @staticmethod
    def read_args():
        parser = argparse.ArgumentParser(description='Finds the most active cookie(s)!')
        parser.add_argument('-f', dest='filename', required=True, type=accessible_file, help='Path to a CSV file')
        parser.add_argument('-d', dest='date', required=True, type=iso_format_date, help='Requested date in ISO format')
        args = parser.parse_args()
        logger.debug(f'Parsed args: {args}')
        return args
