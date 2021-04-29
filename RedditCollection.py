from RedditClient import RedditClient

class RedditCollection(RedditClient):

    def __init__(self):
        super().__init__()
        self.collection_id = None
        self.link_fullname = None
        self.uh_x_modhash_header = None
        self.include_links = None

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


