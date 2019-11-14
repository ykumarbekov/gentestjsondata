import argparser as t
import processor as pr
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

    p = pr.DataProcessor(args)
    p.run_process()


if __name__ == "__main__":
    start()
