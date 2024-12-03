from ..swen610_db_utils import exec_commit, exec_get_all
from ..services.NotificationService import NotificationService
from datetime import datetime

class MessageService:
    def __init__(self):
        self.notification_service = NotificationService()

    def get_user_id(self, username):
        query = '''
            SELECT id FROM users WHERE email = %s
        '''
        result = exec_get_all(query, (username,))
        print(result,'')
        return result[0][0] if result else None

    def send_message(self, to_id, from_id, title, content):
        query = '''
            INSERT INTO messages (title, content, to_id, from_id)
            VALUES (%s, %s, %s, %s)
        '''
        exec_commit(query, (title, content, to_id, from_id))
        self.send_notification(to_id, 'You have received a new message.')

    def get_messages(self, user_id):
        query = '''
            SELECT DISTINCT ON (m.from_id) m.from_id, m.to_id, m.title, m.content, m.sent_at,
                   u1.username as sender_name, u2.username as receiver_name
            FROM messages m
            JOIN users u1 ON m.from_id = u1.id
            JOIN users u2 ON m.to_id = u2.id
            WHERE (m.to_id = %s OR m.from_id = %s) AND m.from_id != m.to_id
            ORDER BY m.from_id, m.sent_at DESC
        '''
        messages = exec_get_all(query, (user_id, user_id))
        messages_list = [{'from_id': m[0], 'to_id': m[1], 'title': m[2], 'content': m[3], 'sent_at': m[4].strftime('%Y-%m-%d %H:%M:%S'), 'sender_name': m[5], 'receiver_name': m[6]} for m in messages]
        return messages_list

    def get_conversation(self, from_id, to_id):
        query = '''
            SELECT m.from_id, m.to_id, m.title, m.content, m.sent_at,
                   u1.name as sender_name, u2.name as receiver_name
            FROM messages m
            JOIN users u1 ON m.from_id = u1.id
            JOIN users u2 ON m.to_id = u2.id
            WHERE (m.from_id = %s AND m.to_id = %s) OR (m.from_id = %s AND m.to_id = %s)
            ORDER BY m.sent_at ASC
        '''
        messages = exec_get_all(query, (from_id, to_id, to_id, from_id))
        messages_list = [{'from_id': m[0], 'to_id': m[1], 'title': m[2], 'content': m[3], 'sent_at': m[4].strftime('%Y-%m-%d %H:%M:%S'), 'sender_name': m[5], 'receiver_name': m[6]} for m in messages]
        return messages_list

    def send_notification(self, user_id, message):
        self.notification_service.send_notification(user_id, message)
