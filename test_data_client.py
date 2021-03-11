import json
from jsonschema import validate

import unittest

from data_client import form_auth_message, form_presence_message, form_quit_message


class TestClientFunc(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.auth_msg = form_auth_message()
        self.prc_msg = form_presence_message()
        self.quit_msg = form_quit_message()

        self.prc_template = {
            "type": "object",
            "properties": {
                "action": {"type": "string"},
                "time": {"type": "number"},
                "type": {"type": "string"},
                "user": {"type": "object"}
            }
        }

        self.auth_template = {
            "type": "object",
            "properties": {
                "action": {"type": "string"},
                "time": {"type": "number"},
                "user": {"type": "object"}
            }
        }

        self.quit_template = {
            "type": "object",
            "properties": {
                "action": {"type": "string"},
                "time": {"type": "number"},
                "type": {"type": "string"},
                "user": {"type": "object"}
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
        msg1 = json.loads(msg)
        try:
            validate(msg1, template)
        except ValueError as err:
            return False
        return True

    def test_json_auth_message(self):
        print("тест аутентификации")
        self.assertEqual(self.json_is_valid(self.auth_msg), True)

    def test_json_presence_message(self):
        print("тест presence")
        self.assertEqual(self.json_is_valid(self.prc_msg), True)

    def test_json_quit_message(self):
        print("тест quit")
        self.assertEqual(self.json_is_valid(self.quit_msg), True)

    def test_auth_message_structure(self):
        print("тест структуры аутентификации")
        self.assertEqual(self.json_structure(self.auth_msg, self.auth_template), True)

    def test_presence_message_structure(self):
        print("тест структуры presence")
        self.assertEqual(self.json_structure(self.prc_msg, self.prc_template), True)

    def test_quit_message_structure(self):
        print("тест структуры quit")
        self.assertEqual(self.json_structure(self.prc_msg, self.quit_template), True)


if __name__ == "__main__":
    unittest.main()
