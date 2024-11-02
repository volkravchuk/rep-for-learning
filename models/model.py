from flask_mongoengine import MongoEngine
from application import app
from datetime import datetime, timezone
import os

app.config['MONGODB_SETTINGS'] = {
    'db': 'history',
    'host': 'localhost',
    'port': 27017,
    'username': os.environ.get('MONGO_USERNAME'),
    'password': os.environ.get('MONGO_PASSWORD'),
    'authentication_source': 'admin'
}

db = MongoEngine(app)

class History(db.Document):
    first_number = db.IntField(required=True)
    operator = db.StringField(required=True)
    second_number = db.IntField(required=True)
    result = db.IntField(required=True)
    calculated = db.DateTimeField(default=lambda: datetime.now(timezone.utc))

    def __repr__(self):
        return f"<History {self.first_number} {self.operator} {self.second_number} = {self.result}>"