import argparse as arg
import os
import sys
from tools import *


class ArgParser(object):

    def __init__(self, d_data):
        self.d_data = d_data
        self.log = create_logger()

    def parse_args(self):
        result = {}
        parser = arg.ArgumentParser(
            prog="gentestdata",
            usage="%(prog)s options",
            description="Utility for generating test JSON data for input schema")

        parser.add_argument(
            "--output-path",
            help="Path for output files. Default: {}".format(self.d_data["output-path"]),
            default=self.d_data["output-path"],
            dest="output_path"
        )
        parser.add_argument(
            "--file-name",
            help="Output filename. Default: {}".format(self.d_data["file-name"]),
            default=self.d_data["file-name"],
            dest="file_name"
        )
        parser.add_argument(
            "--file-count",
            help="Number of generated JSON files. Default: {}".format(self.d_data["file-count"]),
            default=self.d_data["file-count"],
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
            dest="schema"
        )
        parser.add_argument(
            "--output-data-lines",
            help="Number of lines. Default: {}".format(self.d_data["output-data-lines"]),
            default=self.d_data["output-data-lines"],
            dest="output_data_lines"
        )
        parser.add_argument(
            "--clear-output-data",
            help="Flag, to delete -1 or keep -0 previous generated data. Default: {}"
                .format(self.d_data["clear-output-data"]),
            default=self.d_data["clear-output-data"],
            dest="clear_data"
        )

        a = parser.parse_args()
        result["output_path"] = self.output_path_validator(a.output_path)
        result["filename"] = a.file_name
        result["file_count"] = self.files_count_validator(int(a.file_count))
        result["file_prefix"] = a.file_prefix
        result["schema"] = a.schema
        result["output_lines"] = a.output_data_lines
        result["clear_data"] = a.clear_data

        return result

    def output_path_validator(self, p):
        if not os.path.exists(p):
            output_path = os.path.join(os.getcwd(), p)
        else:
            output_path = p
        # *********************
        if not os.path.exists(output_path):
            print("Cannot find: {}".format(output_path))
            self.log.warning("Cannot find: {}".format(output_path))
            sys.exit(-1)
        if not os.path.isdir(output_path):
            print("Output path is not directory")
            self.log.warning("Output path is not directory")
            sys.exit(-1)

        return output_path

    def files_count_validator(self, c):
        if c < 0:
            print("File count parameter negative")
            self.log.warning("File count parameter negative")
            sys.exit(-1)

        return c


