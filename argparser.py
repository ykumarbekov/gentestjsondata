import argparse as arg
from tools import *
import sys


class ArgParser(object):
    '''
    Filename: argparser.py. Class: ArgParser

    The ArgParser uses for parsing program arguments
    Class contains main function:
    - parse_args
        Use parse_args, to parse and validate program arguments

    Constructor
        Input parameter: (dict) d_data - contains values from default configuration file
    '''

    def __init__(self, d_data):
        self.d_data = d_data
        self.log = create_logger()

    def parse_args(self):
        '''
        Parses and validates program arguments
        :return: dict
        '''
        result = {}

        try:

            parser = arg.ArgumentParser(
                prog="gentestdata",
                usage="%(prog)s parameters",
                description="Utility for generating test JSON data for input schema")

            parser.add_argument(
                "--output-path",
                help="Path for output files. Default: {}".format(self.d_data["output-path"]),
                default=self.d_data["output-path"],
                # required=True,
                dest="output_path"
            )
            parser.add_argument(
                "--file-name",
                help="Output filename. Default: {}".format(self.d_data["file-name"]),
                default=self.d_data["file-name"],
                # required=True,
                dest="file_name"
            )
            parser.add_argument(
                "--file-count",
                help="Number of generated JSON files. Default: {}".format(self.d_data["file-count"]),
                default=self.d_data["file-count"],
                # required=True,
                dest="file_count"
            )
            parser.add_argument(
                "--file-prefix",
                choices=["count", "random", "uuid"],
                help="Prefix for output files, use: count|random|uuid. Default: {}".format(self.d_data["file-prefix"]),
                default=self.d_data["file-prefix"],
                dest="file_prefix"
            )
            parser.add_argument(
                "--schema",
                help="JSON Schema for output files, Default: {} file".format(self.d_data["schema"]),
                default=self.d_data["schema"],
                # required=True,
                dest="schema"
            )
            parser.add_argument(
                "--data-lines",
                help="Number of lines for output files. Default: {}".format(self.d_data["data-lines"]),
                default=self.d_data["data-lines"],
                # required=True,
                dest="data_lines"
            )
            parser.add_argument(
                "--clear-output-data",
                choices=["0", "1"],
                help="Flag, for cleaning previous generated data. Default: {}".format(self.d_data["clear-output-data"]),
                default=self.d_data["clear-output-data"],
                dest="clear_data"
            )

            a = parser.parse_args()
            result["output_path"] = self.__output_path_validator(a.output_path)
            result["filename"] = a.file_name
            result["file_count"] = int(self.__files_count_validator(a.file_count))
            result["file_prefix"] = a.file_prefix
            result["schema"] = a.schema
            result["output_lines"] = int(self.__output_count_validator(a.data_lines))
            result["clear_data"] = int(a.clear_data)

        except Exception as ex:
            self.log.error(ex)
            return {}

        return result

    def __output_path_validator(self, p):
        if not os.path.exists(p):
            output_path = os.path.join(os.getcwd(), p)
        else:
            output_path = p

        if not os.path.exists(output_path):
            self.log.warning("Cannot find: {}".format(output_path))
            sys.exit(1)
        if not os.path.isdir(output_path):
            self.log.warning("Output path is not directory")
            sys.exit(1)

        return output_path

    def __output_count_validator(self, n):
        try:
            if int(n) <= 0:
                self.log.warning("Output count parameter is negative. Must above 0")
                sys.exit(1)
        except Exception as ex:
            self.log.error(ex)
            sys.exit(1)
        return n

    def __files_count_validator(self, c):
        try:
            if int(c) < 0:
                self.log.warning("File count parameter is negative. Must be 0 or above")
                sys.exit(1)
        except Exception as ex:
            self.log.error(ex)
            sys.exit(1)

        return c


