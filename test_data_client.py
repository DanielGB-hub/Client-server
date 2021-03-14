import json
from jsonschema import validate
import time
import unittest

from data_client import make_auth_message, make_presence_message, make_quit_message, get_time_fun


class TestClientFunc(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.auth_msg = make_auth_message("C0deMaver1ck", "CorrectHorseBatteryStaple", get_time_fun)
        self.prc_msg = make_presence_message("C0deMaver1ck", "CorrectHorseBatteryStaple", get_time_fun)
        self.quit_msg = make_quit_message("C0deMaver1ck", "CorrectHorseBatteryStaple", get_time_fun)

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
        self.assertEqual(self.json_structure(self.auth_msg, self.quit_template), True)

    #def test_time_auth_message(self):
        #msg_time = int(time.time())
        #msg = make_auth_message("C0deMaver1ck", "CorrectHorseBatteryStaple", lambda: msg_time)


if __name__ == "__main__":
    unittest.main()
