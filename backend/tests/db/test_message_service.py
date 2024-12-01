import unittest
from src.db.services.MessageService import MessageService
from src.db.swen610_db_utils import exec_commit

class TestMessageService(unittest.TestCase):
    def setUp(self):
        self.message_service = MessageService()

    def test_send_message(self):
        self.message_service.send_message(1, 2, 'Hello', 'Hi, how are you?')
        messages = self.message_service.get_messages(2)
        self.assertTrue(any(m['title'] == 'Hello' for m in messages))

    def test_get_messages(self):
        messages = self.message_service.get_messages(1)
        self.assertEqual(len(messages), 3)

if __name__ == '__main__':
    unittest.main()