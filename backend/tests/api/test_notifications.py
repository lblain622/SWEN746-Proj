import unittest
from tests.test_utils import post_rest_call

class TestNotificationAPI(unittest.TestCase):
    def setUp(self):
        self.base_url = 'http://localhost:5000/notify'
        
    def test_notify_message_received(self):
        url = f'{self.base_url}/1/message_received'
        response = post_rest_call(self, url)
        self.assertEqual(response['message'], 'Notification sent successfully.')

    def test_notify_project_assigned(self):
        url = f'{self.base_url}/2/project_assigned'
        response = post_rest_call(self, url)
        self.assertEqual(response['message'], 'Notification sent successfully.')

    def test_notify_project_deadline(self):
        url = f'{self.base_url}/3/project_deadline'
        response = post_rest_call(self, url)
        self.assertEqual(response['message'], 'Notification sent successfully.')

    def test_notify_task_completed(self):
        url = f'{self.base_url}/3/task_completed'
        response = post_rest_call(self, url)
        self.assertEqual(response['message'], 'Notification sent successfully.')

if __name__ == '__main__':
    unittest.main()
