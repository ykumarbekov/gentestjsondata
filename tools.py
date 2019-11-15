import logging
import random as rnd
import uuid
import os


def create_fn_logger(log_name):
    '''
    create_fn_logger uses for initialization file logger
    :param log_name:
    :return: logger
    '''
    logger = logging.getLogger("gentestjsondata-app")
    logger.setLevel(logging.INFO)
    fh = logging.FileHandler(log_name)
    formatter = logging.Formatter('%(asctime)s - %(name)s. %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    # if logger.hasHandlers(): logger.handlers.clear()
    logger.addHandler(fh)

    return logger


def create_logger():
    '''
    create logger uses for initialization simple console logger
    :return: logger
    '''
    logger = logging.getLogger("gentestjsondata-app")
    formatter = logging.Formatter('%(asctime)s - %(name)s. %(levelname)s - %(message)s')
    logger.setLevel(logging.INFO)
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)

    return logger


def rnd_list_value(lst):
    '''
    rnd_list_value uses to choose random value from the List
    :param lst:
    :return: random value
    '''
    if len(lst) > 0:
        return lst[rnd.randint(0, len(lst)-1)]
    else:
        return ""


def output_files(fc, prefix, output_path, filename):
    '''
    output_files uses for generating output files according with input parameters
    :param fc:
    :param prefix:
    :param output_path:
    :param filename:
    :return: filename list <can be empty if one of input values is wrong>
    '''
    f_names = []
    if fc > 0:
        if prefix == "count":
            for n in range(fc):
                f_names.append(os.path.join(output_path, __join_name(str(n), filename)))
        elif prefix == "random":
            for n in range(fc):
                f_names.append(os.path.join(output_path, __join_name(str(rnd.randint(0, 100000)), filename)))
        else:
            for n in range(fc):
                f_names.append(os.path.join(output_path, __join_name(str(uuid.uuid4().hex), filename)))
    return f_names


def clear_folder(f_path, f_name):
    log = create_logger()
    status = 1
    try:
        for r, d, f in os.walk(f_path):
            for ff in f:
                if f_name in ff:
                    fff = os.path.join(r, ff)
                    print("File: {} will be deleted".format(fff))
                    # os.remove(fff)
    except Exception as ex:
        log.error(ex)
        status = 0

    return status


def __join_name(prefix, filename):
    return os.path.splitext(filename)[0] + "_" + prefix + os.path.splitext(filename)[1]

