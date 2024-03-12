from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow import EXCLUDE
from marshmallow import fields

from db.models.video import VideoModel

class VideoAPIGetSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = VideoModel
        unknown = EXCLUDE
    
    id = fields.Int(dump_only=True)
    published_at = fields.String(data_key="publishedAt")