"""
The logging module allows to print messages to the console and/or to a file
during runtime and accross modules and applications (as long as it is the same python instance)

For messages to be logged into a file, a FileHandler must be added to the logger. 
For messages to be shown on the console, a StreamHandler must be created and 
added too.
"""

import logging

# Create a new logger
logger = logging.getLogger('simple_example')
# Set its level to the lowest level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
logger.setLevel(logging.DEBUG)

# Create file handler which logs even debug messages. 
# There is a basic version and a rotating version
#basic_file_handler = logging.FileHandler('spam.log') # basic version
rorating_file_handler = logging.handlers.RotatingFileHandler(
    'spam.log', maxBytes=20, backupCount=5)
rorating_file_handler.setLevel(logging.DEBUG)
# create console handler with a higher log level
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.ERROR)
# create formatter for the layout of messages and add it to the handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)
rorating_file_handler.setFormatter(formatter)
# add the handlers to logger
logger.addHandler(console_handler)
logger.addHandler(rorating_file_handler)

# Optional: Add handlers to the root logger to catch and show calls to it
root = logging.getLogger('')
root.addHandler(file_handler)
root.addHandler(console_handler)

# 'application' code
logger.debug('debug message')
logger.info('info message')
logger.warn('warn message')
logger.error('error message')
logger.critical('critical message')
root.debug("a call to the root logger")


# Note: Rotating file handler allow to control the size of the log file 
# and keep a certain number of backup 
# 
