import logging
from os import getenv

config = {
    'log_level': getenv('MOST_ACTIVE_COOKIE_LOG_LEVEL', logging.INFO)
}