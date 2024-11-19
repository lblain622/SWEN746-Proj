import unittest
from unittest.mock import patch
from flask import Flask
from flask_restful import Api
from src.api.controllers.NotificationController import NotificationController
from src.db.services.NotificationService import NotificationService

class TestNotificationService(unittest.TestCase):
    def setUp(self):
        self.notification_service = NotificationService()

    @patch('src.db.services.NotificationService.NotificationService.send_notification')
    def test_notify_message_received(self, mock_send_notification):
        self.notification_service.notify_message_received(1)
        mock_send_notification.assert_called_with(1, 'You have received a new message.')

    @patch('src.db.services.NotificationService.NotificationService.send_notification')
    def test_notify_project_assigned(self, mock_send_notification):
        self.notification_service.notify_project_assigned(2)
        mock_send_notification.assert_called_with(2, 'You have been assigned a new project.')

    @patch('src.db.services.NotificationService.NotificationService.send_notification')
    def test_notify_project_deadline(self, mock_send_notification):
        self.notification_service.notify_project_deadline(3)
        mock_send_notification.assert_called_with(3, 'Your project deadline is approaching.')

    @patch('src.db.services.NotificationService.NotificationService.send_notification')
    def test_notify_task_completed(self, mock_send_notification):
        self.notification_service.notify_task_completed(4)
        mock_send_notification.assert_called_with(4, 'The task you assigned has been completed.')


if __name__ == '__main__':
    unittest.main()