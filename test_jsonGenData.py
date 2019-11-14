from unittest import *
import jsongendata as jg
import json


class TestJsonGenData(TestCase):

    d_data = [{
                "date": "timestamp",
                "name": "str:rand",
                "type": "str:['client', 'partner', 'government']",
                "age": "int:rand(1, 90)"
                },
                {
                "date": "timestamp",
                "name": "str:rand",
                "type": "str:['client', 'partner', 'government']",
                "age": "int:rand"
                }]

    def test_generate_json_row(self):
        self.assertEqual(
            len(jg.JsonGenData({"schema": str(self.d_data[0])}).generate_json_row(self.d_data[0])), 4)
        self.assertEqual(
            len(jg.JsonGenData({"schema": str(self.d_data[1])}).generate_json_row(self.d_data[1])), 4)


