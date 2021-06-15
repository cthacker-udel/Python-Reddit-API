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
        return body

    def clear_queries(self):

        self.act = None
        self.page = None
        self.uh_x_modhash_header = None
        self.username = None
        self.previous = None
        self.reason = None
        self.content = None
