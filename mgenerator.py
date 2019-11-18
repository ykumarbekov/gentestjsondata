import argparser as t
import processor as pr
import configparser
import sys
from tools import *

config_file = "default.ini"


def start():
    '''
    Main function starts processing, use python3 mgenerator.py arguments
    :return: None
    '''

    log = create_logger()

    if not os.path.exists(config_file):
        log.warning("Cannot find configuration file: {}".format(config_file))
        sys.exit(1)

    # Parsing data from configuration file
    config = configparser.ConfigParser()
    config.read(config_file)
    default_ini_ = config['DEFAULT']

    # Test keys from Default.ini
    if not all(i == j for i, j in zip([k for k in default_ini_.keys()], default_ini_args)):
        log.warning("Cannot validate Default.ini. Possible wrong or incomplete values ")
        sys.exit(1)

    # Parsing program arguments as input parameter - dictionary with values from config file
    arg_parser = t.ArgParser(default_ini_)
    args = arg_parser.parse_args()

    if len(args) == 0:
        log.warning("Cannot run process. Wrong or incomplete program arguments.")
        sys.exit(1)

    # Cleaning output path
    if args["clear_data"] == 1:
        log.warning("Removing all files matched to base name: {} ...".format(args["filename"]))
        clear_folder(args["output_path"], args["filename"])

    # Generating output data, as input parameters - dictionary with parsed values
    pr.DataProcessor(args).run_process()


if __name__ == "__main__":
    start()
