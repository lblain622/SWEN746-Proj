import unittest
from unittest.mock import patch
from flask import Flask
from flask_restful import Api
from src.api.controllers.MessageController import MessageController
from src.db.services.MessageService import MessageService

class TestMessageService(unittest.TestCase):
    def setUp(self):
        self.message_service = MessageService()

    @patch('src.db.services.MessageService.MessageService.send_message')
    def test_send_message(self, mock_send_message):
        self.message_service.send_message(1, 2, 'Hello', 'Hi, how are you?')
        mock_send_message.assert_called_with(1, 2, 'Hello', 'Hi, how are you?')

    @patch('src.db.services.MessageService.MessageService.get_messages')
    def test_get_messages(self, mock_get_messages):
        mock_get_messages.return_value = [
            {"from_id": 1, "to_id": 2, "title": "Hello", "content": "Hi, how are you?"}
        ]
        messages = self.message_service.get_messages(2)
        self.assertEqual(len(messages), 1)
        self.assertEqual(messages[0]['title'], 'Hello')

if __name__ == '__main__':
    unittest.main()