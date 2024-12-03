import unittest
import json

from tests.test_utils import *

class TestService(unittest.TestCase):

    def setUp(self):
        """Initialize DB using API call"""
        post_rest_call(self, 'http://localhost:5000/manage/init')

    def test_create_service(self):
        json_body = {
            "title": "App Development",
            "content": "Mobile application development service",
            "price": 1000.00,
            "user_id": 1
        }

        expected_result = {
            "message": "Service created successfully"
        }

        body_json = json.dumps(json_body)
        api_result = post_rest_call(
            self,
            'http://localhost:5000/services/create',
            params=body_json,
            post_header={'Content-Type': 'application/json'}
        )

        self.assertEqual(api_result, expected_result, 'Service created successfully')

    def test_get_one_service(self):
        expected_result = [
            1,
            "Web Development",
            "Custom web development service",
            "500.00",
            1
        ]

        api_result = get_rest_call(
            self,
            'http://localhost:5000/services/1',
            get_header={'Content-Type': 'application/json'}
        )

        api_result_filtered = [api_result[0], api_result[1], api_result[2], api_result[3], api_result[5]]

        self.assertEqual(api_result_filtered, expected_result, 'The service is found')

    def test_get_all_user_services(self):
        expected_result = [
            1,
            "Web Development",
            "Custom web development service",
            "500.00",
            1
        ]

        api_result = get_rest_call(
            self,
            'http://localhost:5000/services/user/1',
            get_header={'Content-Type': 'application/json'}
        )
        api_result= api_result[0]

        api_result_filtered = [api_result[0], api_result[1], api_result[2], api_result[3], api_result[5]]
        self.assertEqual(api_result_filtered, expected_result, 'The service for a user is found')
    def test_delete_service(self):
        expected_result = {
            "message": "Service deleted successfully"
        }

        api_result = delete_rest_call(
            self,
            'http://localhost:5000/services/delete/1',
            delete_header={'Content-Type': 'application/json'}
        )

        self.assertEqual(api_result, expected_result, 'Service deleted successfully')