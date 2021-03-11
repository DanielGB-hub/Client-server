import json
from jsonschema import validate

import unittest

from data_server import form_auth_server_msg


class TestClientFunc(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.auth_msg = form_auth_server_msg()

        self.auth_resp_template = {
            "properties": {
                "response": {"type": "number"},
                "alert": {"type": "string"}
            }
        }

    @classmethod
    def tearDownClass(self):
        print("tearDown")

    def json_is_valid(self, msg):
        try:
            json_object = json.loads(msg)
        except ValueError as err:
            return False
        return True

    def json_structure(self, msg, template):
        try:
            validate(msg, template)
        except ValueError as err:
            return False
        return True

    def test_json_auth_resp(self):
        print("тест структуры ответа аутентификации")
        self.assertEqual(self.json_structure(self.auth_msg, self.auth_resp_template), True)

    def test_json_presence_msg(self):
        print("тест presence")
        self.assertEqual(self.json_is_valid(self.auth_msg), True)


if __name__ == "__main__":
    unittest.main()
