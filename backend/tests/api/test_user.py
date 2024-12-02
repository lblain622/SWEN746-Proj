import unittest
import json

from tests.test_utils import *

class TestUser(unittest.TestCase):

    def setUp(self):
        """Initialize DB using API call"""
        post_rest_call(self, 'http://localhost:5000/manage/init')

    def test_login(self):
        json_body = {
            "name":"John Doe",
            "password":"password123"
        }

        expected_result = {
            "message": "Success"
        }

        body_json = json.dumps(json_body)
        api_result = post_rest_call(
            self,
            'http://localhost:5000/login',
            params=body_json,
            post_header={'Content-Type': 'application/json'}
        )

        self.assertEqual(api_result, expected_result, 'Login success')

    def test_create_user(self):
        json_body = {
            "name":"vanecat",
            "password":"kittycat",
            "email":"kittycat@gmail.com",
        }

        expected_result = {
            'message':'User created successfully'
        }

        body_json = json.dumps(json_body)
        api_result = post_rest_call(

            self,
            'http://localhost:5000/create/user',
            params=body_json,

            post_header={'Content-Type': 'application/json'}
        )

        self.assertEqual(api_result, expected_result, 'Creation success')

    def test_get_one_user(self):
        expected_result = [
            1,
            "John Doe",
            "password123",
            "john.doe@example.com"
        ]

        api_result = get_rest_call(

            self,
            'http://localhost:5000/obtain/user/1',

            get_header={'Content-Type': 'application/json'}
        )

        api_result_filtered = [api_result[0], api_result[1], api_result[2], api_result[3]]

        self.assertEqual(api_result_filtered, expected_result, 'The user is found')

    def test_update_user(self):
        json_body = {
            'name':'John Doe123',
            'password':'password1234',
            "email":"joh.doe@example.com",
        }

        expected_result = {
            'message':'User updated successfully'
        }

        body_json = json.dumps(json_body)
        api_result = put_rest_call(
            self,

            'http://localhost:5000/edit/user/1',
            params=body_json,

            put_header={'Content-Type': 'application/json'}
        )

        self.assertEqual(api_result, expected_result, 'Update success')

    def test_delete_user(self):
        expected_result = {
            'message':'User deleted successfully'
        }

        api_result = delete_rest_call(
            self,
            'http://localhost:5000/delete/user/1',
            delete_header={'Content-Type': 'application/json'}
        )

        self.assertEqual(api_result, expected_result, 'Delete success')
