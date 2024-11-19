from src.db.swen610_db_utils import exec_commit, exec_get_all
from src.db.services.NotificationService import NotificationService

class MessageService:
    def __init__(self):
        self.notification_service = NotificationService()

    def send_message(self, from_id, to_id, title, content):
        query = '''
            INSERT INTO messages (title, content, to_id, from_id)
            VALUES (%s, %s, %s, %s)
        '''
        exec_commit(query, (title, content, to_id, from_id))
        print(f"Message sent from user {from_id} to user {to_id}: {title} - {content}")
        self.send_notification(to_id, 'You have received a new message.')

    def get_messages(self, user_id):
        query = '''
            SELECT from_id, to_id, title, content
            FROM messages
            WHERE to_id = %s OR from_id = %s
        '''
        messages = exec_get_all(query, (user_id, user_id))
        print(f"Getting messages for user {user_id}")
        return messages

    def send_notification(self, user_id, message):
        self.notification_service.send_notification(user_id, message)
