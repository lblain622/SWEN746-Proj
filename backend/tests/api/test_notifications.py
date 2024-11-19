import unittest
from unittest.mock import patch
from flask import Flask
from flask_restful import Api
from src.api.controllers.NotificationController import NotificationController
from src.db.services.NotificationService import NotificationService


class TestNotificationAPI(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.api = Api(self.app)
        self.api.add_resource(NotificationController, '/notify/<int:user_id>/<string:notification_type>')
        self.client = self.app.test_client()

    @patch('src.api.controllers.NotificationController.NotificationService.notify_message_received')
    def test_notify_message_received(self, mock_notify_message_received):
        response = self.client.post('/notify/1/message_received')
        self.assertEqual(response.status_code, 200)
        mock_notify_message_received.assert_called_with(1)

    @patch('src.api.controllers.NotificationController.NotificationService.notify_project_assigned')
    def test_notify_project_assigned(self, mock_notify_project_assigned):
        response = self.client.post('/notify/2/project_assigned')
        self.assertEqual(response.status_code, 200)
        mock_notify_project_assigned.assert_called_with(2)

    @patch('src.api.controllers.NotificationController.NotificationService.notify_project_deadline')
    def test_notify_project_deadline(self, mock_notify_project_deadline):
        response = self.client.post('/notify/3/project_deadline')
        self.assertEqual(response.status_code, 200)
        mock_notify_project_deadline.assert_called_with(3)

    @patch('src.api.controllers.NotificationController.NotificationService.notify_task_completed')
    def test_notify_task_completed(self, mock_notify_task_completed):
        response = self.client.post('/notify/4/task_completed')
        self.assertEqual(response.status_code, 200)
        mock_notify_task_completed.assert_called_with(4)

if __name__ == '__main__':
    unittest.main()
