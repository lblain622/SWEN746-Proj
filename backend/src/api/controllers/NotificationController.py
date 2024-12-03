from flask_restful import Resource
from db.services.NotificationService import NotificationService

class NotificationController(Resource):
    def __init__(self):
        self.notification_service = NotificationService()

    def post(self, user_id, notification_type):
        try:
            if notification_type == 'message_received':
                self.notification_service.notify_message_received(user_id)
            elif notification_type == 'project_assigned':
                self.notification_service.notify_project_assigned(user_id)
            elif notification_type == 'project_deadline':
                self.notification_service.notify_project_deadline(user_id)
            elif notification_type == 'task_completed':
                self.notification_service.notify_task_completed(user_id)
            else:
                return {'message': 'Invalid notification type'}, 400
            return {'message': 'Notification sent successfully.'}, 200
        except Exception as e:
            return {'message': str(e)}, 500
