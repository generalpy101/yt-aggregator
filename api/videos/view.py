from api.videos import videos_bp
from api.videos.schema import VideoAPIGetSchema
from core.views.base import BaseView
from db.models.video import VideoModel

class VideoView(BaseView):
    model = VideoModel
    order_by = VideoModel.published_at.desc()
    get_schema = VideoAPIGetSchema
    
videos_bp.add_url_rule("/videos", view_func=VideoView.as_view("videos"), strict_slashes=False)