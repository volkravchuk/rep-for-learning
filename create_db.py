from application import app
from models.model import db

with app.app_context():
    db.create_all()