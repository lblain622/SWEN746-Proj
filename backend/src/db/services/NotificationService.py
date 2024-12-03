from ..swen610_db_utils import exec_commit, exec_get_all

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

    def get_notifications(self, user_id):
        query = '''
            SELECT title, content, created_at
            FROM notifications
            WHERE user_id = %s
        '''
        notifications = exec_get_all(query, (user_id,))
        notifications_list = [{'title': n[0], 'content': n[1], 'created_at': n[2]} for n in notifications]
        print(f"Getting notifications for user {user_id}")
        return notifications_list

    def get_user_id(self, username):
        query = '''
            SELECT id FROM users WHERE email = %s
        '''
        result = exec_get_all(query, (username,))
        return result[0][0] if result else None
