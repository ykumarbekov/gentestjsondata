from unittest import TestCase, main
from tools import *


class TestTools(TestCase):

    d_data = [{
            "a1": "timestamp",
            "a2": "str:rand",
            "a3": "str:['client', 'partner', 'government']",
            "a4": "int:rand(1, 90)"
        },
        {
            "a1": "timestamp",
            "a2": "str:rand",
            "a3": "int:['client', 'partner', 'government']",
            "a4": "int:rand"
        },
        {
            "a1": "['el1','el2']", "a2": "int:[10,20,30]", "a3": "int:rand", "a4": "str:rand"
        },
        {
            "a1": "['el1','el2']", "a2": "int:[10,20,30]", "a3": "int:rand", "a4": "int:rand(1,1)"
        },
        {
            "a1": "['el1','el2']", "a2": "int", "a3": "int:rand", "a4": "int:rand(1,10)"
        }
    ]

    def test_json_row_validator(self):
        for k in self.d_data:
            self.assertEqual(len(json_row_generator(k)), len(k),
                             msg="Non-parsing elements: {}".format(k))

    def test_output_files(self):
        f_lst = output_files(3, "count", "/path", "data.json")
        self.assertEqual(len(f_lst), 3)
        self.assertListEqual(
            f_lst,
            ["/path/data_0.json", "/path/data_1.json", "/path/data_2.json"],
            msg="Actual List doesn't equal to generated list"
        )

    def test_file_names(self):
        self.assertEqual(test_file_names("data.json", "data_100000000.json"), True)


if __name__ == "__main__":
    main()
