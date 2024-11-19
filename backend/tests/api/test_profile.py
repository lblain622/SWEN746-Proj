import unittest
import json
from tests.test_utils import *

class TestProfile(unittest.TestCase):
    def test_GetProfile(self):
        print("Get a profile")

        expected = [1,'John','Doe',30,'M','S12345']
        actual = get_rest_call(self,'http://127.0.0.1:5000/profile/1')
        self.assertEqual(expected,actual)


    def test_CreateProfile(self):
        print("Creating a new profile")
        data = {
            'first_name': 'Bob',
            'last_name': 'Doe',
            'age': 30,
            'sex': 'M',
            'student_id': 'BD123',
            'user_id': 3
        }
        jdata = json.dumps(data)

        result=post_rest_call(self,'http://127.0.0.1:5000/profile',params=jdata,post_header={'content-type': 'application/json'})
        msg_expected = {"message": "Profile Created"}
        self.assertEqual(msg_expected,result)

    def test_UpdateProfile(self):
        print("Updating profile")
        data = {
            'first_name': 'Belle',
            'last_name': 'Martin',
            'age': 31,
            'sex': 'F',
            'user_id': 3,
        }
        jdata = json.dumps(data)
        result = put_rest_call(self,'http://127.0.0.1:5000/profile/3',jdata,put_header={'content-type': 'application/json'})
        msg_expected = {"message": "Profile updated successfully"}
        self.assertEqual(msg_expected,result)

    def test_DeleteProfile(self):
        print("Deleting a Profile")
        result = delete_rest_call(self,'http://127.0.0.1:5000/profile/2')
        msg_expected = {"message": "Profile deleted successfully"}
        self.assertEqual(msg_expected,result)
