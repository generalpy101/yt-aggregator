import os
import time
import requests
import logging

from datetime import datetime
from dotenv import load_dotenv

from api import create_app
from configs import DevConfig
from core.schemas.youtube_search_schema import YoutubeVideoSchema, YoutubeSearchSchema, YoutubeIdSchema, YoutubeSnippetSchema
from core.schemas.video_schema import VideoAPIGetSchema
from db.models.video import VideoModel

load_dotenv()

VIDEO_AGGREGATION_FREQUENCY = os.getenv("VIDEO_AGGREGATION_FREQUENCY", 10)
VIDEO_AGGREGATION_API = os.getenv("VIDEO_AGGREGATION_API", "https://www.googleapis.com/youtube/v3/")
VIDEO_AGGREGATION_API_KEY = os.getenv("VIDEO_AGGREGATION_API_KEY", "YOUR_API_KEY")
VIDEO_SEARCH_QUERY = os.getenv("VIDEO_SEARCH_QUERY", "songs")

app = create_app(config_class=DevConfig)
logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

def aggregate_videos(published_after):
    logger.info("Aggregating videos...")
    response = requests.get(f"{VIDEO_AGGREGATION_API}search?q={VIDEO_SEARCH_QUERY}&part=snippet&type=video&order=date&key={VIDEO_AGGREGATION_API_KEY}&publishedAfter={published_after}")
    
    return response.json()

def current_time_RFC3339():
    return datetime.utcnow().isoformat("T") + "Z"
    
def main():
    logger.info("Starting video aggregation worker...")
    started_at = current_time_RFC3339()

    last_requested_at = started_at

    while True:
        try:
            data = aggregate_videos(last_requested_at)
            # Load data into the schema
            search_results = YoutubeSearchSchema().load(data)
            
            with app.app_context():
                # Save the data to the database
                for item in search_results["items"]:
                    video = YoutubeVideoSchema().load(item).get("snippet")
                    video = VideoAPIGetSchema().load(video)
                    video_model = VideoModel(**video)
                    video_model.save_to_db()

            last_requested_at = current_time_RFC3339()
        except KeyboardInterrupt:
            logger.warning("Stopping video aggregation worker...")
        except Exception as e:
            logger.exception(f"An error occurred: {e}")
        finally:
            time.sleep(VIDEO_AGGREGATION_FREQUENCY)
