import os
import random as rnd
import uuid


class JsonGenData(object):

    def __init__(self, d_data):
        self.d_data = d_data
        self.fc = int(d_data["file_count"])
        self.prefix = d_data["file_prefix"]
        self.output_path = d_data["output_path"]
        self.filename = d_data["filename"]

    def file_schema_parser(self):
        print("Start generating schema from file")
        print("Output files: ")
        for f in self.output_files():
            print("File: {}".format(f))

    def data_schema_parser(self):
        print("Start generating schema from data")
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

    def run_generator(self):
        if os.path.exists(self.d_data["schema"]):
            self.file_schema_parser()
        else:
            self.data_schema_parser()
        return

