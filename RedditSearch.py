from RedditClient import RedditClient

class RedditSearch(RedditClient):

    def __init__(self):
        self.subreddit = None

        self.after = None
        self.before = None
        self.category = None
        self.count = None
        self.include_facets = None
        self.limit = None
        self.q = None
        self.restrict_sr = None
        self.show = None
        self.sort = None
        self.sr_detail = None
        self.t = None
        self.type = None


    def generate_queries(self):

        body = {}

        if self.after != None:
            body['after'] = self.after
        if self.before != None:
            body['before'] = self.before
        if self.category != None:
            body['category'] = self.category
        if self.count != None:
            body['count'] = self.count
        if self.include_facets != None:
            body['include_facets'] = self.include_facets
        if self.limit != None:
            body['limit'] = self.limit
        if self.q != None:
            body['q'] = self.q
        if self.restrict_sr != None:
            body['restrict_sr'] = self.restrict_sr
        if self.show != None:
            body['show'] = self.show
        if self.sort != None:
            body['sort'] = self.sort
        if self.sr_detail != None:
            body['sr_detail'] = self.sr_detail
        if self.t != None:
            body['t'] = self.t
        if self.type != None:
            body['type'] = self.type
        return body

    def clear_queries(self):
        self.after = None
        self.before = None
        self.category = None
        self.count = None
        self.include_facets = None
        self.limit = None
        self.q = None
        self.restrict_sr = None
        self.show = None
        self.sort = None
        self.sr_detail = None
        self.t = None
        self.type = None