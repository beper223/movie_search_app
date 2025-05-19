import logging

logging.basicConfig(filename="logs/errors.log", level=logging.ERROR)

def log_error(error):
    logging.error("Exception occurred", exc_info=error)