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

        expected_result = [{'message': 'Review created successfully'}, 200]
        

        body_json = json.dumps(json_body)
        api_result = post_rest_call(
            self,
            'http://localhost:5000/create/review',
            params=body_json,
            post_header={'Content-Type': 'application/json'}
        )

        self.assertEqual(api_result, expected_result, 'Review creation success')

    def test_get_review(self):
        expected_result = [
        [
            2,
            4,
            "Good work, but room for improvement.",
            2,
            2
        ]
    ]

        api_result = get_rest_call(
            self,
            'http://localhost:5000/obtain/review/2',
            get_header={'Content-Type': 'application/json'}
        )

        self.assertEqual(api_result, expected_result, 'Review retrieval success')

    def test_update_review(self):
        json_body = {
            "rating": 5,
            "feedback": "Updated review: Excellent service!",
            "service_id": 1,
            "user_id": 2,
        }

        expected_result = [{'message': 'Review updated successfully'}, 200]
            

        body_json = json.dumps(json_body)
        api_result = put_rest_call(
            self,
            'http://localhost:5000/edit/review/1',
            params=body_json,
            put_header={'Content-Type': 'application/json'}
        )

        self.assertEqual(api_result, expected_result, 'Review update success')

    def test_delete_review(self):
        expected_result = [{'message': 'Review deleted successfully'}, 200]
            
        

        api_result = delete_rest_call(
            self,
            'http://localhost:5000/delete/review/1',
            delete_header={'Content-Type': 'application/json'}
        )

        self.assertEqual(api_result, expected_result, 'Review deletion success')

