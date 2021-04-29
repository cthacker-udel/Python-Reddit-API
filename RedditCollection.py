from RedditClient import RedditClient

class RedditCollection(RedditClient):

    def __init__(self):
        super().__init__()
        self.collection_id = None
        self.link_fullname = None
        self.uh_x_modhash_header = None
        self.include_links = None
        self.display_layout = None
        self.sr_fullname = None
        self.title = None
        self.description = None

    def generate_body(self):
        body = {}
        if self.collection_id != None:
            body['collection_id'] = self.collection_id
        if self.link_fullname != None:
            body['link_fullname'] = self.link_fullname
        if self.uh_x_modhash_header != None:
            body['uh / X-Modhash header'] = self.uh_x_modhash_header
        if self.include_links != None:
            body['include_links'] = self.include_links
        if self.description != None:
            body['description'] = self.description
        if self.display_layout != None:
            body['display_layout'] = self.display_layout
        if self.sr_fullname != None:
            body['sr_fullname'] = self.sr_fullname
        if self.title != None:
            body['title'] = self.title
        return body


