from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow import EXCLUDE

from db.models.video import VideoModel

class VideoAPIGetSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = VideoModel
        unknown = EXCLUDE