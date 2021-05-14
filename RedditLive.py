from RedditClient import RedditClient

class RedditLive(RedditClient):

    def __init__(self):
        super().__init__()
        self.names = []




    def generate_queries(self):
        body = {}
        if len(self.names) > 0:
            body['names'] = ','.join(self.names)
        return body

    def clear_queries(self):
        self.names = []
