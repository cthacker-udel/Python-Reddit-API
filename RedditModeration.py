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
        self.location = None
        self.only = None
        self.how = None
        self.id = None
        self.sticky = None
        self.api_type = None
        self.uh_x_modhash_header = None

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
        if self.only != None:
            queries['only'] = self.only
        if self.id != None:
            queries['id'] = self.id
        if self.sticky != None:
            queries['sticky'] = self.sticky
        if self.api_type != None:
            queries['api_type'] = self.api_type
        if self.how != None:
            queries['how'] = self.how
        if self.uh_x_modhash_header != None:
            queries['uh / X-Modhash header'] = self.uh_x_modhash_header
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
        self.how = None
        self.id = None
        self.sticky = None
        self.api_type = None
        self.uh_x_modhash_header = None