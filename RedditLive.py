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
        self.thread_name = None
        self.link = None
        self.user_name = None
        self.permissions = None
        self.type = None
        self.id = None

        self.count = None
        self.limit = None
        self.show = None
        self.sr_detail = None
        self.after = None
        self.before = None

        self.update_id = None




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
        if self.link != None:
            body['link'] = self.link
        if self.user_name != None:
            body['name'] = self.user_name
        if self.permissions != None:
            body['permissions'] = self.permissions
        if self.type != None:
            body['type'] = self.type
        if self.id != None:
            body['id'] = self.id
        if self.count != None:
            body['count'] = self.count
        if self.after != None:
            body['after'] = self.after
        if self.before != None:
            body['before'] = self.before
        if self.limit != None:
            body['limit'] = self.limit
        if self.show != None:
            body['show'] = self.show
        if self.sr_detail != None:
            body['sr_detail'] = self.sr_detail
        return body


    def get_thread_name(self):
        return self.thread_name

    def clear_queries(self):
        self.names = []
        self.api_type = None
        self.description = None
        self.nsfw = None
        self.resources = None
        self.title = None
        self.uh_x_modhash_header = None
        self.thread_name = None
        self.link = None
        self.user_name = None
        self.permissions = None
        self.type = None
        self.id = None
        self.count = None
        self.limit = None
        self.show = None
        self.sr_detail = None
        self.after = None
        self.before = None
