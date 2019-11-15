from unittest import TestCase, main
from tools import *


class TestTools(TestCase):

    d_data = [{
        "date": "timestamp",
        "name": "str:rand",
        "type": "str:['client', 'partner', 'government']",
        "age": "int:rand(1, 90)"
    },
        {
            "date": "timestamp",
            "name": "str:rand",
            "type": "float:['client', 'partner', 'government']",
            "age": "int:rand"
        }]

    def test_json_row_validator(self):
        self.assertEqual(len(json_row_generator(self.d_data[0])), 4)
        self.assertEqual(
            len(json_row_generator(self.d_data[1])), 4,
            msg="Schema contains non-parsing elements"
        )

    def test_output_files(self):
        f_lst = output_files(
            3,
            "count",
            "/path",
            "data.json"
        )

        self.assertEqual(len(f_lst), 3)
        self.assertListEqual(
            f_lst,
            ["/path/data_0.json", "/path/data_1.json", "/path/data_2.json"],
            msg="Error: Actual List doesn't equal to generated list"
        )

    def test_file_names(self):
        self.assertEqual(
            test_file_names(
                "data.json",
                "data_100000000.json"
            ), True)


if __name__ == "__main__":
    main()
