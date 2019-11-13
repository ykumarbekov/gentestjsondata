import argparser as t
import jsongen as jg
import configparser
import os
import sys
from tools import *


def start():

    log = create_logger()

    if not os.path.exists("default.ini"):
        print("Cannot find configuration file: default.ini")
        log.warning("Cannot find configuration file: default.ini")
        sys.exit(-1)

    config = configparser.ConfigParser()
    config.read("default.ini")
    arg_parser = t.ArgParser(config['DEFAULT'])
    args = arg_parser.parse_args()

    json_gnr = jg.JsonGenData(args)
    json_gnr.run_generator()

    for k, v in args.items():
        print("{}: {}".format(k, v))


if __name__ == "__main__":
    start()
