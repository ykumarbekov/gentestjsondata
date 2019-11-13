import argparser as t
import configparser
import os
import sys
import logging


def start():

    if not os.path.exists("default.ini"):
        print("Cannot find default.ini")
        sys.exit(-1)

    config = configparser.ConfigParser()
    config.read("default.ini")
    arg_parser = t.ArgParser(config['DEFAULT'])
    args = arg_parser.parse_args()

    for k, v in args.items():
        print("{}: {}".format(k, v))


if __name__ == "__main__":
    start()
