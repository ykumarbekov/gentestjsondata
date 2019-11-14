import jsongendata as jg
from tools import *
import os
import random as rnd
import uuid
import json
import sys


class DataProcessor(object):

    def __init__(self, d_data):
        self.d_data = d_data
        self.fc = int(d_data["file_count"])
        self.prefix = d_data["file_prefix"]
        self.output_path = d_data["output_path"]
        self.filename = d_data["filename"]
        self.cnt_output = int(d_data["output_lines"])
        self.log = create_logger()
        self.json_gnr = jg.JsonGenData(d_data)

    def run_process(self):
        if len(self.output_files()) == 0:
            self.log.info("Started generating data for console output")
            for i in range(self.cnt_output):
                print(self.json_gnr.run_generator())
        else:
            self.log.info("Started generating data for output files")
            try:
                for f in self.output_files():
                    self.log.info("Saving in file {} ...".format(f))
                    with open(f, "w+") as ff:
                        for i in range(self.cnt_output):
                            json.dump(self.json_gnr.run_generator(), ff)
                            ff.write("\n")
            except Exception as ex:
                self.log.error(ex)
                sys.exit(1)

    def output_files(self):
        f_names = []
        if self.fc > 0:
            if self.prefix == "count":
                for n in range(self.fc):
                    f_names.append(os.path.join(self.output_path, str(n)+"_"+self.filename))
            elif self.prefix == "random":
                for n in range(self.fc):
                    f_names.append(os.path.join(self.output_path, str(rnd.randint(0, 100000)) + "_" + self.filename))
            else:
                for n in range(self.fc):
                    f_names.append(os.path.join(self.output_path, str(uuid.uuid4().hex) + "_" + self.filename))
        return f_names
