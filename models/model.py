from flask_sqlalchemy import SQLAlchemy
from application import app
from datetime import datetime, timezone

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///history.db"
db = SQLAlchemy(app)

class History(db.Model):
    id = db.Column(db.Integer, primary_key=True) 
    first_number = db.Column(db.Integer, nullable = False)
    operator = db.Column(db.String, nullable = False)
    second_number = db.Column(db.Integer, nullable = False)
    result = db.Column(db.Integer, nullable = False)
    calculated = db.Column(db.DateTime, default = lambda: datetime.now(timezone.utc))

    def __repr__(self):
        return f"<{self.first_number}>"