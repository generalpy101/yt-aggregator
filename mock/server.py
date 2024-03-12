import random
from enum import Enum
from datetime import datetime
from flask import Flask

from mock.schema import YoutubeVideoSchema, YoutubeSearchSchema, YoutubeIdSchema, YoutubeSnippetSchema

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


def generate_video_items(amount=5):
    '''
    Generate a list of random video items
    '''
    items = []
    for i in range(amount):
        yotube_id_data = YoutubeIdSchema().load({
            'kind': 'youtube#video',
            'videoId': generate_id(11)
        })

        snippet = {
            'publishedAt': datetime.now().isoformat(),
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
        }

        snippet_data = YoutubeSnippetSchema().load(snippet)

        video = {
            'kind': ResponseKindEnum.YOUTUBE_VIDEO.value,
            'etag': generate_etag(),
            'id': yotube_id_data,
            "snippet": snippet_data,
            "liveBroadcastContent": "none",
            "channelTitle": "Channel Title",
            "publishTime": datetime.now().isoformat()
        }
        items.append(video)
    return items


@app.route('/videos')
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

    return YoutubeSearchSchema().dumps(data)

if __name__ == '__main__':
    app.run(debug=True, port=8081, host='0.0.0.0')