import unittest
import json
from tests.test_utils import *

class TestUser(unittest.TestCase):

    def setUp(self):  
        """Initialize DB using API call"""
        post_rest_call(self, 'http://localhost:5000/manage/init')

    # def test_login(self):
    #     json_body = { 
    #         "username":"john_doe",
    #         "password":"password123"
    #     }

    #     expected_result = {
    #         "messasge": "Success"
    #     }

    #     body_json = json.dumps(json_body)
    #     api_result = post_rest_call(
    #         self,
    #         'http://localhost:5000/user/login',
    #         params=body_json,
    #         post_header={'Content-Type': 'application/json'}
    #     )

    #     self.assertEqual(api_result, expected_result, 'Login success')

    # def test_create_user(self):
    #     json_body = { 
    #         "username":"vanecat",
    #         "password":"kittycat"
    #     }

    #     expected_result = {
    #         'message':'User created successfully'
    #     }

    #     body_json = json.dumps(json_body)
    #     api_result = post_rest_call(
    #         self, 
    #         'http://localhost:5000/user/create',
    #         params=body_json, 
    #         post_header={'Content-Type': 'application/json'}
    #     )

    #     self.assertEqual(api_result, expected_result, 'Creation success')

    # def test_get_one_user(self):
    #     expected_result = [
    #         1,
    #         "john_doe",
    #         "password123",
    #         True
    #     ]

    #     api_result = get_rest_call(
    #         self, 
    #         'http://localhost:5000/users/1', 
    #         get_header={'Content-Type': 'application/json'}
    #     )

    #     api_result_filtered = [api_result[0], api_result[1], api_result[2], api_result[4]]
        
    #     self.assertEqual(api_result_filtered, expected_result, 'The user is found')

    # def test_update_user(self):
    #     json_body = {
    #         'username':'john_doe',
    #         'password':'password123'
    #     }

    #     expected_result = {
    #         'message':'User updated successfully'
    #     }

    #     body_json = json.dumps(json_body)
    #     api_result = put_rest_call(
    #         self,
    #         'http://localhost:5000/user/edit/1', 
    #         params=body_json, 
    #         put_header={'Content-Type': 'application/json'}
    #     )

    #     self.assertEqual(api_result, expected_result, 'Update success')