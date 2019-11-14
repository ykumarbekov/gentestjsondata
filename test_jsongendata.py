import jsongendata as jg
import unittest


class TestJsonGenData(unittest.TestCase):

    d_data = {
        "schema": "{\"date\":\"timestamp\", \"name\": \"str:rand\", \"type\":\"str:['client', 'partner', 'government']\", \"age\": \"int:rand(1, 90)\"}"
    }
    json_gnr = jg.JsonGenData(d_data)

    def test_generate_json_row(self):
        result = self.json_gnr.run_generator()
        self.assertEqual(result, )


if __name__ == "__main__":
    unittest.main()
