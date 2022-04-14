from common.db import db
from datetime import datetime
from datetime import timezone
from dataclasses import dataclass


@dataclass
class PostModel(db.Model):
    __tablename__ = "posts"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    content = db.Column(db.String(50), nullable=False)
    poster_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    create_date = db.Column(
        db.DateTime, default=datetime.now(timezone.utc), nullable=False
    )

    def add_post(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_post(cls, id):
        return cls.query.filter_by(id=id).first()
