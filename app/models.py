from pymongo import MongoClient
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

# MongoDB connection
client = MongoClient('mongodb://localhost:27017/')
db = client['user_auth_db']
users = db['users']

class User:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password_hash = generate_password_hash(password)
        self.created_at = datetime.utcnow()

    @staticmethod
    def get_by_username(username):
        return users.find_one({'username': username})

    @staticmethod
    def get_by_email(email):
        return users.find_one({'email': email})

    def save(self):
        user_data = {
            'username': self.username,
            'email': self.email,
            'password_hash': self.password_hash,
            'created_at': self.created_at
        }
        return users.insert_one(user_data)

    @staticmethod
    def verify_password(password_hash, password):
        return check_password_hash(password_hash, password)
