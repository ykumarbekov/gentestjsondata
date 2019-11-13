import logging


def create_logger():
    logger = logging.getLogger("gen-test-json-data-app")
    logger.setLevel(logging.INFO)
    fh = logging.FileHandler("gen-json-data.log")
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)

    if logger.hasHandlers():
        logger.handlers.clear()

    logger.addHandler(fh)
    return logger

