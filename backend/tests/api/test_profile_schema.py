import unittest
from backend.src.db.services.ProfileService import *
import json
from backend.tests.test_utils import *

class TestProfileService(unittest.TestCase):
    def test_CreateProfile(self):
        print("Creating a new profile")
        data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'age': 30,
            'sex': 'male',
            'student_id': 'JD123',
            'user_id': 1
        }
        jdata = json.dumps(data)

        post_rest_call(self,'http://localhost:5000/profile/',params=jdata,post_header={'content-type': 'application/json'})
        expected = [{'id': 1, 'first_name': 'John', 'last_name': 'Doe', 'age': 30, 'sex': 'male', 'student_id': 'S12345', 'user_id': 1}]
        actual = get_rest_call(self,'http://localhost:5000/profile/3')
        self.assertEqual(expected, actual)
