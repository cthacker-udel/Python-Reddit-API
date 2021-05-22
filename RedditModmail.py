from RedditClient import RedditClient

class RedditModmail(RedditClient):

    def __init__(self):
        super().__init__()
        self.entity = None
        self.state = None
        self.after = None
        self.limit = None
        self.sort = None
        self.subreddit = None


    def generate_queries(self):
        body = {}

        if self.entity != None:
            body['entity'] = self.entity
        if self.state != None:
            body['state'] = self.state
        if self.after != None:
            body['after'] = self.after
        if self.limit != None:
            body['limit'] = self.limit
        if self.sort != None:
            body['sort'] = self.sort


    def clear_queries(self):
        self.entity = None
        self.state = None
        self.after = None
        self.limit = None
        self.sort = None