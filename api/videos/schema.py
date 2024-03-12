from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

from db.models.video import VideoModel

class VideoAPIGetSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = VideoModel
        unknown = "EXCLUDE"