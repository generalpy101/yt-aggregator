from db import db
from db.models.base import Base
from sqlalchemy.dialects.postgresql import JSON

class VideoModel(Base):
    __tablename__ = 'videos'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    description = db.Column(db.String(2047))
    published_at = db.Column(db.DateTime)
    thumbnails = db.Column(JSON)

    def __init__(self, *args, **kwargs):
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()
