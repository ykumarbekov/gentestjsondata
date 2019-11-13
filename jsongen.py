import os
import random as rnd
import uuid
import json
from tools import *
import sys
import time


class JsonGenData(object):

    def __init__(self, d_data):
        self.d_data = d_data
        self.fc = int(d_data["file_count"])
        self.prefix = d_data["file_prefix"]
        self.output_path = d_data["output_path"]
        self.filename = d_data["filename"]
        self.log = create_logger()
        self.schema = d_data["schema"]

    def file_schema_parser(self):
        print("Start generating schema from file")
        # *********************
        print("Output files: ")
        for f in self.output_files():
            print("File: {}".format(f))

    def data_schema_parser(self):
        print("Start generating schema from data")
        self.generate_json_row(self.json_parser(self.schema))
        # *********************
        print("Output files: ")
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

    def json_parser(self, json_data):
        try:
            return json.loads(json_data)
        except Exception as ex:
            print(ex)
            self.log.error(ex)
            sys.exit(-100)

    def generate_json_row(self, dd):
        ddd = {}
        cnt = 0
        for k, v in dd.items():
            print("{}:{}".format(k, v))
            if len(v.split(":")) == 1:
                if v == "timestamp":
                    ddd[k] = time.time()
                    cnt += 1
                elif v == "str":
                    ddd[k] = ""
                    cnt += 1
                elif v == "int":
                    ddd[k] = None
                    cnt += 1
                elif v != "timestamp" and v != "str" and v != "int" and "[" and "]" in str(v):
                    ddd[k] = rnd_list_value(v.rstrip("]").lstrip("[").split(","))
                    cnt += 1
            elif len(v.split(":")) == 2:
                if v.split(":")[0] == "str" and v.split(":")[1] == "rand":
                    pass

        return ddd

    def run_generator(self):
        if os.path.exists(self.d_data["schema"]):
            self.file_schema_parser()
        else:
            self.data_schema_parser()
        return

