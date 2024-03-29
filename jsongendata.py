import json
from tools import *
import sys


class JsonGenData(object):
    '''
    Filename: jsongendata.py. Class: JsonGenData

    The JsonGenData uses for parsing input JSON schema and generating output row
    Class contains next functions:
    - generate_json_row
    - run_generator

    Constructor
        Initializes schema parameter from file or from command arguments
        Input parameter: d_data - dictionary contains program arguments
    '''

    def __init__(self, d_data):
        self.d_data = d_data
        self.log = create_logger()

        if os.path.exists(self.d_data["schema"]):
            try:
                with open(self.d_data["schema"]) as schema_f:
                    self.schema = schema_f.read()
            except Exception as ex:
                self.log.error(ex)
                sys.exit(1)
        else:
            self.schema = self.d_data["schema"]

    def __json_parser(self, json_data):
        try:
            return json.loads(json_data)
        except Exception as ex:
            self.log.error(ex)
            return {}

    def __generate_json_row(self, dd):
        '''
        Local function
        Validates, parses and generates output dictionary with all necessary values
        :param (dict) dd:
        :return: dict
        '''
        try:
            ddd = json_row_generator(dd)
        except Exception as ex:
            self.log.error(ex)
            sys.exit(1)

        if len(ddd) != len(self.__json_parser(self.schema)):
            self.log.warning("Number of processed elements: {} doesn't equal actual elements: {}".format(len(ddd), len(self.__json_parser(self.schema))))
            return {}

        return ddd

    def run_generator(self):
        '''
        Validates, parses and generates output dictionary with all necessary values
        :return: dict
        '''
        return self.__generate_json_row(self.__json_parser(self.schema))


