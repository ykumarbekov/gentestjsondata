import jsongendata as jg
from tools import *
import os
import random as rnd
import uuid


class DataProcessor(object):

    def __init__(self, d_data):
        self.d_data = d_data
        self.fc = int(d_data["file_count"])
        self.prefix = d_data["file_prefix"]
        self.output_path = d_data["output_path"]
        self.filename = d_data["filename"]
        self.cnt_output = d_data["output_data_lines"]
        self.log = create_logger()
        self.json_gnr = jg.JsonGenData(d_data)

    def run_process(self):
        if len(self.output_files()) == 0:
            print("Output to console")
            print(self.json_gnr.run_generator())
        else:
            print("Output to files ")
            print(self.json_gnr.run_generator())
            for f in self.output_files():
                print("File: {}".format(f))

    def output_files(self):
        f_names = []
        if self.fc > 0:
            if self.prefix == "count":
                for n in range(self.fc):
                    f_names.append(os.path.join(self.output_path, str(n)+"_"+self.filename))
            elif self.d_data["file_prefix"] == "random":
                for n in range(self.fc):
                    f_names.append(os.path.join(self.output_path, str(rnd.randint(0, 100000)) + "_" + self.filename))
            else:
                for n in range(self.fc):
                    f_names.append(os.path.join(self.output_path, str(uuid.uuid4().hex) + "_" + self.filename))
        return f_names
