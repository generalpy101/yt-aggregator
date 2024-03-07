import os
import time
import requests

from datetime import datetime, timedelta
from dotenv import load_dotenv

load_dotenv()

VIDEO_AGGREGATION_FREQUENCY = os.getenv("VIDEO_AGGREGATION_FREQUENCY", 10)
VIDEO_AGGREGATION_API = os.getenv("VIDEO_AGGREGATION_API", "https://www.googleapis.com/youtube/v3/")
VIDEO_AGGREGATION_API_KEY = os.getenv("VIDEO_AGGREGATION_API_KEY", "YOUR_API_KEY")
VIDEO_SEARCH_QUERY = os.getenv("VIDEO_SEARCH_QUERY", "python")

def aggregate_videos(published_after):
    print("Aggregating videos...")
    response = requests.get(f"{VIDEO_AGGREGATION_API}search?q={VIDEO_SEARCH_QUERY}&part=snippet&type=video&order=date&q=python&key={VIDEO_AGGREGATION_API_KEY}&publishedAfter={published_after}")
    print(response.json())
    
def current_time_RFC3339():
    return datetime.utcnow().isoformat("T") + "Z"
    
def main():
    started_at = current_time_RFC3339()

    last_requested_at = started_at

    while True:
        try:
            print(last_requested_at)
            aggregate_videos(last_requested_at)
            last_requested_at = current_time_RFC3339()
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            time.sleep(VIDEO_AGGREGATION_FREQUENCY)
            
main()