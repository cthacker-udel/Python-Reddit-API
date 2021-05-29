from RedditClient import RedditClient

class RedditSubreddit(RedditClient):

    def __init__(self):
        self.where = None
        self.subreddit = None

        self.after = None
        self.before = None
        self.count = None
        self.limit = None
        self.show = None
        self.sr_detail = None
        self.user = None


    def generate_queries(self):

        body = {}

        if self.after != None:
            body['after'] = self.after
        if self.before != None:
            body['before'] = self.before
        if self.count != None:
            body['count'] = self.count
        if self.limit != None:
            body['limit'] = self.limit
        if self.show != None:
            body['show'] = self.show
        if self.sr_detail != None:
            body['sr_detail'] = self.sr_detail
        if self.user != None:
            body['user'] = self.user

    def clear_queries(self):

        self.after = None
        self.before = None
        self.count = None
        self.limit = None
        self.show = None
        self.sr_detail = None
        self.user = None