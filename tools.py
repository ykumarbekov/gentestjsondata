import logging
import random as rnd
import uuid
import os
import sys
import time


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
    if logger.hasHandlers():
        logger.handlers.clear()
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
    if logger.hasHandlers():
        logger.handlers.clear()
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
                f_names.append(os.path.join(output_path, __join_prefix_to_name(str(n), filename)))
        elif prefix == "random":
            for n in range(fc):
                f_names.append(os.path.join(output_path, __join_prefix_to_name(str(rnd.randint(0, 100000)), filename)))
        else:
            for n in range(fc):
                f_names.append(os.path.join(output_path, __join_prefix_to_name(str(uuid.uuid4().hex), filename)))
    return f_names


def clear_folder(f_path, f_name):
    '''
    clear_folder for removing files from target folder
    :param f_path:
    :param f_name:
    :return: status: 1 - successful or 0 - unsuccessful
    '''
    log = create_logger()
    status = 1
    try:
        for r, d, f in os.walk(f_path):
            for ff in f:
                if test_file_names(f_name, ff):
                    fff = os.path.join(r, ff)
                    log.info("File: {} will be deleted".format(fff))
                    os.remove(fff)
    except Exception as ex:
        log.error(ex)
        status = 0

    return status


def test_file_names(f1, f2):
    if os.path.splitext(f1)[0] in os.path.splitext(f2)[0] and \
       os.path.splitext(f1)[1] in os.path.splitext(f2)[1]:
        return True
    else:
        return False


def __join_prefix_to_name(prefix, filename):
    return os.path.splitext(filename)[0] + "_" + prefix + os.path.splitext(filename)[1]


def json_row_generator(dd):
    '''
    json_row_generator - validates, parses and generates output dictionary with all necessary values
    :param dd:
    :return:
    '''
    log = create_logger()
    ddd = {}
    try:
        for k, v in dd.items():
            if len(v.split(":")) == 1 or (len(v.split(":")) == 2 and len(v.split(":")[1]) == 0):
                if "timestamp" in v and ":" in v:
                    ddd[k] = time.time()
                elif "timestamp" in v:
                    ddd[k] = time.time()
                elif "str" in v and ":" not in v:
                    ddd[k] = ""
                elif "str" in v and ":" in v:
                    ddd[k] = ""
                elif "int" in v and ":" not in v:
                    ddd[k] = None
                elif "int" in v and ":" not in v:
                    ddd[k] = None
                elif v != "timestamp" and v != "str" and v != "int" and "[" and "]" in str(v):
                    ddd[k] = rnd_list_value(v.rstrip("]").lstrip("[").split(","))
            # ------------------------------------------------
            elif len(v.split(":")) == 2:
                if v.split(":")[0] == "str" and "rand" in v.split(":")[1] and len(v.split(":")[1]) == 4:
                    ddd[k] = str(uuid.uuid4().hex)
                elif v.split(":")[0] == "int" and "rand" in v.split(":")[1] and len(v.split(":")[1]) == 4:
                    ddd[k] = str(rnd.randint(0, 10000))
                elif v.split(":")[0] == "str" and "rand" in v.split(":")[1] and ("(" and ")" in v.split(":")[1]):
                    pass
                elif v.split(":")[0] == "int" and "rand" in v.split(":")[1] and ("(" and ")" in v.split(":")[1]):
                    n1 = int(v.split(":")[1][5:len(v.split(":")[1])-1].split(",")[0])
                    n2 = int(v.split(":")[1][5:len(v.split(":")[1])-1].split(",")[1])
                    ddd[k] = str(rnd.randint(n1, n2))
                elif (v.split(":")[0] == "str" or v.split(":")[0] == "int") and "[" and "]" in v.split(":")[1]:
                    ddd[k] = rnd_list_value(v.split(":")[1].rstrip("]").lstrip("[").split(","))
    except Exception as ex:
        log.error(ex)
        return {}

    return ddd
