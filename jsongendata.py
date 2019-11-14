import os
import uuid
import json
from tools import *
import sys
import time


class JsonGenData(object):

    def __init__(self, d_data):
        self.d_data = d_data
        self.log = create_logger()
        # ***************************************
        if os.path.exists(self.d_data["schema"]):
            try:
                with open(self.d_data["schema"]) as schema_f:
                    self.schema = schema_f.read()
            except Exception as ex:
                self.log.error(ex)
                sys.exit(1)
        else:
            self.schema = self.d_data["schema"]

    def json_parser(self, json_data):
        try:
            return json.loads(json_data)
        except Exception as ex:
            self.log.error(ex)
            sys.exit(1)

    def generate_json_row(self, dd):
        ddd = {}
        cnt = 0
        try:
            for k, v in dd.items():
                # print("{} - {}".format(k, v))
                if len(v.split(":")) == 1 or (len(v.split(":")) == 2 and len(v.split(":")[1]) == 0):
                    if "timestamp" in v and ":" in v:
                        self.log.warning("Schema element: {}:{} contains empty char ':' Fixed.".format(k, v))
                        ddd[k] = time.time()
                        cnt += 1
                    elif "timestamp" in v:
                        ddd[k] = time.time()
                        cnt += 1
                    elif "str" in v and ":" not in v:
                        ddd[k] = ""
                        cnt += 1
                    elif "str" in v and ":" in v:
                        self.log.warning("Schema element: {}:{} contains empty char ':' Fixed.".format(k, v))
                        ddd[k] = ""
                        cnt += 1
                    elif "int" in v and ":" not in v:
                        ddd[k] = None
                        cnt += 1
                    elif "int" in v and ":" not in v:
                        self.log.warning("Schema element: {}:{} contains empty char ':' ".format(k, v))
                        ddd[k] = None
                        cnt += 1
                    elif v != "timestamp" and v != "str" and v != "int" and "[" and "]" in str(v):
                        ddd[k] = rnd_list_value(v.rstrip("]").lstrip("[").split(","))
                        cnt += 1
                # ***************************
                elif len(v.split(":")) == 2:
                    if v.split(":")[0] == "str" and "rand" in v.split(":")[1] and len(v.split(":")[1]) == 4:
                        ddd[k] = str(uuid.uuid4().hex)
                        cnt += 1
                    if v.split(":")[0] == "int" and "rand" in v.split(":")[1] and len(v.split(":")[1]) == 4:
                        ddd[k] = str(random.randint(0, 10000))
                        cnt += 1
                    elif v.split(":")[0] == "str" and "rand" in v.split(":")[1] and ("(" and ")" in v.split(":")[1]):
                        print("You cannot use {} with str type".format(v.split(":")[1]))
                        self.log.warning("You cannot use {} with str type".format(v.split(":")[1]))
                        sys.exit(1)
                    elif v.split(":")[0] == "int" and "rand" in v.split(":")[1] and ("(" and ")" in v.split(":")[1]):
                        n1 = int(v.split(":")[1][5:len(v.split(":")[1])-1].split(",")[0])
                        n2 = int(v.split(":")[1][5:len(v.split(":")[1])-1].split(",")[1])
                        ddd[k] = str(random.randint(n1, n2))
                        cnt += 1
                    elif (v.split(":")[0] == "str" or v.split(":")[0] == "int") and "[" and "]" in v.split(":")[1]:
                        ddd[k] = rnd_list_value(v.split(":")[1].rstrip("]").lstrip("[").split(","))
                        cnt += 1
        except Exception as ex:
            self.log.error(ex)
            sys.exit(1)

        if cnt != len(ddd):
            print("Number of processed elements: {} doesn't equal actual elements: {}".format(cnt, len(ddd)))
            self.log.warning("Number of processed elements: {} doesn't equal actual elements: {}".format(cnt, len(ddd)))
            sys.exit(1)

        return ddd

    def run_generator(self):
        return self.generate_json_row(self.json_parser(self.schema))


