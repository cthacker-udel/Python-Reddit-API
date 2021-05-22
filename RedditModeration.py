from RedditClient import RedditClient

class RedditModeration(RedditClient):

    def __init__(self):
        super().__init__()
        self.after = None
        self.before = None
        self.count = None
        self.limit = None
        self.mod = None
        self.show = None
        self.sr_detail = None
        self.type = None
        self.subreddit = None

    def generate_queries(self):
        queries = {}
        if self.after != None:
            queries['after'] = self.after
        if self.before != None:
            queries['before'] = self.before
        if self.count != None:
            queries['count'] = self.count
        if self.limit != None:
            queries['limit'] = self.limit
        if self.mod != None:
            queries['mod'] = self.mod
        if self.show != None:
            queries['show'] = self.show
        if self.sr_detail != None:
            queries['sr_detail'] = self.sr_detail
        if self.type != None:
            queries['type'] = self.type
        return queries


    def clear_queries(self):
        self.after = None
        self.before = None
        self.count = None
        self.limit = None
        self.mod = None
        self.show = None
        self.sr_detail = None
        self.type = None