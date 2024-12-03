import unittest
from tests.test_utils import post_rest_call, get_rest_call
import json

class TestMessageAPI(unittest.TestCase):
    def setUp(self):
        self.base_url = 'http://localhost:5000/messages'

    def test_send_message(self):
        url = self.base_url
        params = {
            "from_id": 1,
            "to_id": 2,
            "title": 'Hello',
            "content": "Hi, how are you?"
        }
        response = post_rest_call(self, url, params=json.dumps(params), post_header={'Content-Type': 'application/json'},expected_code=201)
        self.assertEqual(response['message'], 'Message sent successfully')

    def test_get_messages(self):
        url = f'{self.base_url}/2'
        response = get_rest_call(self, url)
        self.assertEqual(len(response['messages']), 3)
        self.assertIn('sender_name', response['messages'][0])
        self.assertIn('receiver_name', response['messages'][0])

if __name__ == '__main__':
    unittest.main()
