import jsongendata as jg
from tools import *
import json
import sys


class DataProcessor(object):
    '''
    Filename: processor.py. Class: DataProcessor

    The DataProcessor uses for generating output random data
    Class contains main function:
    - run_process
        Using: run_process(d_data), where d_data - dictionary with input arguments

    Constructor
        Initialize class variables and creates additional object: JsonGenData
        JsonGenData - uses for parsing input json schema and generating output row
    '''

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
        '''
        run_process starts generating and saves data in files
        before saving it validates schema and raises exception if schema is not valid
        :return: None
        '''
        output_f = output_files(
            self.fc,
            self.prefix,
            self.output_path,
            self.filename
        )
        if len(output_f) == 0:
            self.log.info("Started generating data for console output")
            for i in range(self.cnt_output):
                print(self.json_gnr.run_generator())
        else:
            self.log.info("Started generating data for output files")
            try:
                for f in output_f:
                    '''
                    Validating input schema by generating one test row
                    if schema incorrect it returns empty dict and raises Exception
                    '''
                    if self.cnt_output > 0:
                        if len(self.json_gnr.run_generator()) == 0:
                            raise Exception("Stop data processing. Exit")
                    '''
                    ------------------------------------------------
                    '''
                    self.log.info("Saving in file {} ...".format(f))
                    with open(f, "w+") as ff:
                        for i in range(self.cnt_output):
                            json.dump(self.json_gnr.run_generator(), ff)
                            ff.write("\n")
                    self.log.info("Finished.")
            except Exception as ex:
                self.log.error(ex)
                sys.exit(1)


