from RedditClient import RedditClient

class RedditWidget(RedditClient):

    def __init__(self):

        self.widget_id = None
        self.subreddit = None
        self.filepath = None
        self.mimetype = None


    def generate_queries(self):
        body = {}
        if self.filepath != None:
            body['filepath'] = self.filepath
        if self.mimetype != None:
            body['mimetype'] = self.mimetype
        return body