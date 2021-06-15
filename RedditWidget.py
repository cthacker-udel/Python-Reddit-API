from RedditClient import RedditClient

class RedditWidget(RedditClient):

    def __init__(self):

        self.widget_id = None
        self.subreddit = None
        self.filepath = None
        self.mimetype = None
        self.section = None
        self.progressive_images = None
        self.json = None


    def generate_queries(self):
        body = {}
        if self.filepath != None:
            body['filepath'] = self.filepath
        if self.mimetype != None:
            body['mimetype'] = self.mimetype
        if self.json != None:
            body['json'] = self.json
        if self.progressive_images != None:
            body['progressive_images'] = self.progressive_
        return body