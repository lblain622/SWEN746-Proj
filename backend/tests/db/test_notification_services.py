import unittest
from src.db.services.NotificationService import NotificationService

class TestNotificationService(unittest.TestCase):
    def setUp(self):
        self.notification_service = NotificationService()


    def test_notify_message_received(self):
        self.notification_service.notify_message_received(1)
        notifications = self.notification_service.get_notifications(1)
        self.assertTrue(any(n['content'] == 'You have received a new message.' for n in notifications))

    def test_notify_project_assigned(self):
        self.notification_service.notify_project_assigned(2)
        notifications = self.notification_service.get_notifications(2)
        self.assertTrue(any(n['content'] == 'You have been assigned a new project.' for n in notifications))

    def test_notify_project_deadline(self):
        self.notification_service.notify_project_deadline(3)
        notifications = self.notification_service.get_notifications(3)
        self.assertTrue(any(n['content'] == 'Your project deadline is approaching.' for n in notifications))

    def test_notify_task_completed(self):
        self.notification_service.notify_task_completed(1)
        notifications = self.notification_service.get_notifications(1)
        self.assertTrue(any(n['content'] == 'The task you assigned has been completed.' for n in notifications))

if __name__ == '__main__':
    unittest.main()