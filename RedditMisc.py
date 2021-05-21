from RedditClient import RedditClient

class RedditMisc(RedditClient):

    def __init__(self):
        super().__init__()
        self.url = None
        self.scopes = None
        self.subreddit = None


    def generate_queries(self):
        body = {}
        if self.url != None:
            body['url'] = self.url
        if self.scopes != None:
            body['scopes'] = self.scopes
        return body

    def clear_queries(self):
        self.url = None
        self.scopes = None