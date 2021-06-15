from RedditClient import RedditClient

class RedditWiki(RedditClient):

    def __init__(self):

        self.subreddit = None
        self.act = None
        self.page = None
        self.uh_x_modhash_header = None
        self.username = None
        self.previous = None
        self.reason = None
        self.content = None
        self.revision = None
        self.page = None
        self.after = None
        self.before = None
        self.count = None
        self.limit = None
        self.show = None
        self.sr_detail = None


    def generate_queries(self):

        body = {}

        if self.username != None:
            body['username'] = self.username
        if self.uh_x_modhash_header != None:
            body['uh / X-Modhash header'] = self.uh_x_modhash_header
        if self.page != None:
            body['page'] = self.page
        if self.act != None:
            body['act'] = self.act
        if self.previous != None:
            body['previous'] = self.previous
        if self.reason != None:
            body['reason'] = self.reason
        if self.content != None:
            body['content'] = self.content
        if self.revision != None:
            body['revision'] = self.revision
        if self.page != None:
            body['page'] = self.page
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
        return body

    def clear_queries(self):

        self.act = None
        self.page = None
        self.uh_x_modhash_header = None
        self.username = None
        self.previous = None
        self.reason = None
        self.content = None
        self.page = None
        self.after = None
        self.before = None
        self.count = None
        self.limit = None
        self.show = None
        self.sr_detail = None
