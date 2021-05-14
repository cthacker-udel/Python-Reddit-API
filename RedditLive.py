from RedditClient import RedditClient

class RedditLive(RedditClient):

    def __init__(self):
        super().__init__()
        self.names = []
        self.api_type = None
        self.description = None
        self.nsfw = None
        self.resources = None
        self.title = None
        self.uh_x_modhash_header = None




    def generate_queries(self):
        body = {}
        if len(self.names) > 0:
            body['names'] = ','.join(self.names)
        if self.api_type != None:
            body['api_type'] = self.api_type
        if self.description != None:
            body['description'] = self.description
        if self.nsfw != None:
            body['nsfw'] = self.nsfw
        if self.resources != None:
            body['resources'] = self.resources
        if self.title != None:
            body['title'] = self.title
        if self.uh_x_modhash_header != None:
            body['uh / X-Modhash header'] = self.uh_x_modhash_header
        return body

    def clear_queries(self):
        self.names = []
