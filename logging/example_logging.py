"""
The logging module allows to print messages to the console and/or to a file
during runtime and accross modules and applications (as long as it is the same python instance)

For messages to be logged into a file, a FileHandler must be added to the logger. 
For messages to be shown on the console, a StreamHandler must be created and 
added too.
"""

import logging
from logging.handlers import RotatingFileHandler

# Create a new logger
logger = logging.getLogger('simple_example')
# Set its level to the lowest level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
logger.setLevel(logging.DEBUG)

# Create file handler which logs even messages. 
# There is a basic version and a rotating version
basic_file_handler = logging.FileHandler('spam.log') # basic version
# Fancy version that creates a new file every 20 bytes and only keep 5 files 
# at max in addition to the current (overwrites the oldest beyond 5 files)
rorating_file_handler = RotatingFileHandler(
    'rotate_spam.log', maxBytes=100, backupCount=5)

# Set the sensitivity of the handler
rorating_file_handler.setLevel(logging.DEBUG)
basic_file_handler.setLevel(logging.INFO)
# create console handler with a higher log level
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.ERROR)
# create formatter for the layout of messages and add it to the handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s '
                              '- %(message)s')
console_handler.setFormatter(formatter)
rorating_file_handler.setFormatter(formatter)
# add the handlers to logger
logger.addHandler(console_handler)
logger.addHandler(rorating_file_handler)

# Optional: Add handlers to the root logger to catch and show calls to it
root = logging.getLogger()
root.addHandler(basic_file_handler)
root.addHandler(console_handler)

# 'application' code
logger.debug('My debug message')
logger.info('My info message')
logger.warn('My warn message')
logger.error('My error message')
logger.critical('My critical message')
root.debug("My call to the root logger")
root.info("My call to the root logger with info level")
root.error("My call to the root logger with error level")

