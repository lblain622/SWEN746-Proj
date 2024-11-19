from src.db.swen610_db_utils import exec_commit

class NotificationService:
    def send_notification(self, user_id, message):
        query = '''
            INSERT INTO notifications (title, content, user_id)
            VALUES (%s, %s, %s)
        '''
        exec_commit(query, ('Notification', message, user_id))
        print(f"Notification sent to user {user_id}: {message}")

    def notify_message_received(self, user_id):
        self.send_notification(user_id, 'You have received a new message.')

    def notify_project_assigned(self, user_id):
        self.send_notification(user_id, 'You have been assigned a new project.')

    def notify_project_deadline(self, user_id):
        self.send_notification(user_id, 'Your project deadline is approaching.')

    def notify_task_completed(self, user_id):
        self.send_notification(user_id, 'The task you assigned has been completed.')
