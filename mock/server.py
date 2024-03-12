import random
import os
from enum import Enum
from datetime import datetime, timedelta
from flask import Flask, jsonify

from core.schemas.youtube_search_schema import YoutubeVideoSchema, YoutubeSearchSchema, YoutubeIdSchema, YoutubeSnippetSchema


VIDEO_AGGREGATION_FREQUENCY = os.getenv("VIDEO_AGGREGATION_FREQUENCY", 10)

app = Flask(__name__)

RESULTS_PER_PAGE = 5


class ResponseKindEnum(Enum):
    '''
    Enum for response kind
    '''
    YOUTUBE_RESPONSE = 'youtube#searchListResponse'
    YOUTUBE_VIDEO = 'youtube#videoListResponse'


def generate_etag():
    '''
    Generate a random etag
    '''
    return ''.join(random.choice('0123456789abcdef') for i in range(32))


def generate_id(length=5):
    '''
    Generate a list of random video ids
    '''
    return ''.join(random.choice('0123456789abcdef') for i in range(length)) 

def generate_random_date_in_interval():
    # Generate a randome interval between now and VIDEO_AGGREGATION_FREQUENCY
    random_interval = random.randint(0, VIDEO_AGGREGATION_FREQUENCY)
    
    date = datetime.now() - timedelta(seconds=random_interval)
    
    # Convert date to RFC3339
    # Eg: 2024-03-07T09:30:22Z
    date = date.isoformat().split('.')[0] + "Z"
    return date


def generate_video_items(amount=5):
    '''
    Generate a list of random video items
    '''
    items = []
    for _ in range(amount):
        yotube_id_data = YoutubeIdSchema().load({
            'kind': 'youtube#video',
            'videoId': generate_id(11)
        })

        snippet = {
            'publishedAt': generate_random_date_in_interval(),
            'channelId': generate_id(24),
            'title': 'Video Title',
            'description': 'Video Description',
            'thumbnails': {
                'default': {
                    'url': 'https://via.placeholder.com/120x90.png'
                },
                'medium': {
                    'url': 'https://via.placeholder.com/320x180.png'
                },
                'high': {
                    'url': 'https://via.placeholder.com/480x360.png'
                }
            },
            "liveBroadcastContent": "none",
            "channelTitle": "Channel Title",
            "publishTime": generate_random_date_in_interval()
        }

        snippet_data = YoutubeSnippetSchema().load(snippet)

        video = {
            'kind': ResponseKindEnum.YOUTUBE_VIDEO.value,
            'etag': generate_etag(),
            'id': yotube_id_data,
            "snippet": snippet_data,
        }
        items.append(video)
    return items


@app.route('/search')
def videos():
    '''
    Generates a mock response for youtube videos api
    Data is randomised
    '''
    total_results = random.randint(10, 100)

    video_items = generate_video_items(RESULTS_PER_PAGE)

    video_items_data = YoutubeVideoSchema(many=True).load(video_items)

    response = {
        'kind': ResponseKindEnum.YOUTUBE_VIDEO.value,
        'etag': generate_etag(),
        'nextPageToken': generate_id(6),
        'regionCode': 'US',
        'pageInfo': {
            'totalResults': total_results,
            'resultsPerPage': RESULTS_PER_PAGE
        },
        'items': video_items_data
    }

    # Loadings the response data into a schema to ensure it is valid
    data = YoutubeSearchSchema().load(response)

    return jsonify(YoutubeSearchSchema().dump(data))

if __name__ == '__main__':
    app.run(debug=True, port=8081, host='0.0.0.0')