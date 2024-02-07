from logger import logger
from app import MostActiveCookieApp
from arg_parser import ArgumentParser
from exceptions import BadInputException

if __name__ == '__main__':   
    try:
        args = ArgumentParser.read_args()
        app = MostActiveCookieApp(args.filename)
        top_used_cookies = app.get_top_used_cookies(args.date)
    except BadInputException as e:
        logger.error(e)
        exit(-1)
    print('\n'.join(top_used_cookies))
