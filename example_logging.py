
import logging
from logging.handlers import RotatingFileHandler

logger=logging.getLogger()

log_file = "log.txt"
file_handler = RotatingFileHandler(log_file, maxBytes=1024 ** 2,
                                                backupCount=3)
formatter = logging.Formatter("%(levelname)s - %(asctime)s - %(name)s "
                            "- %(message)s")
file_handler.setFormatter(formatter)
logger.setLevel(logging.DEBUG)
logger.addHandler(file_handler)

logger.debug("test")