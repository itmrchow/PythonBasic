from common.db import db
from datetime import datetime


class PostModel(db.Model):
    __tablename__ = "posts"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    content = db.Column(db.String(50), nullable=False)
    poster_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    create_date = db.Column(db.DateTime, default=datetime.now, nullable=False)
