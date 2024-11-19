import unittest
import json
from tests.test_utils import *

class TestReview(unittest.TestCase):

    def setUp(self):  
        """Initialize DB using API call"""
        post_rest_call(self, 'http://localhost:5000/manage/init')

    def test_create_review(self):
        json_body = {
            "rating": 4,
            "feedback": "Great service, very satisfied!",
            "service_id": 1,
            "user_id": 2,
        }

        expected_result = {
            "message": "Review created successfully"
        }

        body_json = json.dumps(json_body)
        api_result = post_rest_call(
            self,
            'http://localhost:5000/review/create',
            params=body_json,
            post_header={'Content-Type': 'application/json'}
        )

        self.assertEqual(api_result, expected_result, 'Review creation success')

    def test_get_review(self):
        expected_result = {
            "service_id": 1,
            "user_id": 2,
            "rating": 4,
            "comment": "Great service, very satisfied!"
        }

        api_result = get_rest_call(
            self,
            'http://localhost:5000/review/obtain/1',
            get_header={'Content-Type': 'application/json'}
        )

        self.assertEqual(api_result, expected_result, 'Review retrieval success')

    def test_update_review(self):
        json_body = {
            "rating": 5,
            "comment": "Updated review: Excellent service!"
        }

        expected_result = {
            "message": "Review updated successfully"
        }

        body_json = json.dumps(json_body)
        api_result = put_rest_call(
            self,
            'http://localhost:5000/review/edit/1',
            params=body_json,
            put_header={'Content-Type': 'application/json'}
        )

        self.assertEqual(api_result, expected_result, 'Review update success')

    def test_delete_review(self):
        expected_result = {
            "message": "Review deleted successfully"
        }

        api_result = delete_rest_call(
            self,
            'http://localhost:5000/review/delete/1',
            delete_header={'Content-Type': 'application/json'}
        )

        self.assertEqual(api_result, expected_result, 'Review deletion success')

