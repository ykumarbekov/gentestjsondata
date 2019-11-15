import argparser as t
import processor as pr
import configparser
import sys
from tools import *

config_file = "default.ini"


def start():

    log = create_logger()

    if not os.path.exists(config_file):
        log.warning("Cannot find configuration file: {}".format(config_file))
        sys.exit(1)

    # Parsing data from configuration file
    config = configparser.ConfigParser()
    config.read(config_file)

    # Parsing program arguments as input parameter - dictionary with values from config file
    arg_parser = t.ArgParser(config['DEFAULT'])
    args = arg_parser.parse_args()

    # Cleaning output path
    if args["clear_data"] == 1:
        log.warning("Removing all files matched: {} on output path...".format(args["filename"]))
        clear_folder(args["output_path"], args["filename"])

    # Generating output data, as input parameters - dictionary with parsed values
    pr.DataProcessor(args).run_process()

    '''
    for i in output_files(
        args["file_count"],
        args["file_prefix"],
        args["output_path"],
        args["filename"]
    ):
        print("File: {}".format(i))
    '''


if __name__ == "__main__":
    start()
