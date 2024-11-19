import unittest
from unittest.mock import patch
from flask import Flask
from flask_restful import Api
from src.api.controllers.MessageController import MessageController
from src.db.services.MessageService import MessageService

class TestMessageAPI(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.api = Api(self.app)
        self.api.add_resource(MessageController, '/messages', '/messages/<int:user_id>')
        self.client = self.app.test_client()

    @patch('src.api.controllers.MessageController.MessageService.send_message')
    def test_send_message(self, mock_send_message):
        response = self.client.post('/messages', json={
            'from_id': 1,
            'to_id': 2,
            'title': 'Hello',
            'content': 'Hi, how are you?'
        })
        self.assertEqual(response.status_code, 200)
        mock_send_message.assert_called_with(1, 2, 'Hello', 'Hi, how are you?')

    @patch('src.api.controllers.MessageController.MessageService.get_messages')
    def test_get_messages(self, mock_get_messages):
        mock_get_messages.return_value = [
            {"from_id": 1, "to_id": 2, "title": "Hello", "content": "Hi, how are you?"}
        ]
        response = self.client.get('/messages/2')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json['messages']), 1)
        self.assertEqual(response.json['messages'][0]['title'], 'Hello')

if __name__ == '__main__':
    unittest.main()
