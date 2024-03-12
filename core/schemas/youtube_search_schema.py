from marshmallow import Schema, fields

class YoutubeIdSchema(Schema):
    kind = fields.String(required=True)
    videoId = fields.String(required=True)
    
class YoutubeSnippetSchema(Schema):
    publishedAt = fields.String(required=True)
    channelId = fields.String(required=True)
    title = fields.String(required=True)
    description = fields.String(required=True)
    thumbnails = fields.Dict(required=True)
    channelTitle = fields.String(required=True)
    liveBroadcastContent = fields.String(required=True)
    publishTime = fields.String(required=True)

class YoutubeVideoSchema(Schema):
    kind = fields.String(required=True)
    etag = fields.String(required=True)
    id = fields.Nested(YoutubeIdSchema, required=True)
    snippet = fields.Nested(YoutubeSnippetSchema, required=True)
    
class YoutubeSearchSchema(Schema):
    kind = fields.String(required=True)
    etag = fields.String(required=True)
    nextPageToken = fields.String(required=False)
    regionCode = fields.String(required=True)
    pageInfo = fields.Dict(required=True)
    items = fields.List(fields.Nested(YoutubeVideoSchema), required=True)