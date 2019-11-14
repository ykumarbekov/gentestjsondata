import logging
import random


def create_fn_logger():
    logger = logging.getLogger("gen-test-json-data-app")
    logger.setLevel(logging.INFO)
    fh = logging.FileHandler("gen-json-data.log")
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)

    if logger.hasHandlers():
        logger.handlers.clear()

    logger.addHandler(fh)
    return logger


def create_logger():
    logger = logging.getLogger("gentestjsondata-app")
    formatter = logging.Formatter('%(asctime)s - %(name)s. %(levelname)s - %(message)s')
    logger.setLevel(logging.INFO)
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)

    return logger


def rnd_list_value(lst):
    if len(lst) > 0:
        return lst[random.randint(0, len(lst)-1)]
    else:
        return ""
