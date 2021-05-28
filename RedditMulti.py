from RedditClient import RedditClient

class RedditMulti(RedditClient):

    def __init__(self):
        self.description_md = None
        self.display_name = None
        self.expand_srs = None
        self._from = None
        self.to = None
        self.uh_x_modhash_header = None
        self.user_name

    def generate_queries(self):

        body = {}

        if self.description_md != None:
            body['description_md'] = self.description_md
        if self.display_name != None:
            body['display_name'] = self.display_name
        if self.expand_srs != None:
            body['expand_srs'] = self.expand_srs
        if self._from != None:
            body['from'] = self._from
        if self.to != None:
            body['to'] = self.to
        if self.uh_x_modhash_header != None:
            body['uh / X-Modhash header'] = self.uh_x_modhash_header
        return body


    def clear_queries(self):

        self.description_md = None
        self.display_name = None
        self.expand_srs = None
        self._from = None
        self.to = None
        self.uh_x_modhash_header = None
