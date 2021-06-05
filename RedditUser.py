from RedditClient import RedditClient

class RedditUser(RedditClient):


    def __init__(self):
        self.account_id = None
        self.api_type = None
        self.name = None
        self.uh_x_modhash_header = None


    def generate_queries(self):
        body = {}
        if self.account_id != None:
            body['account_id'] = self.account_id
        if self.api_type != None:
            body['api_type'] = 'json'
        if self.name != None:
            body['name'] = self.name
        if self.uh_x_modhash_header != None:
            body['uh / X-Modhash header']
        return body

    def clear_queries(self):
        self.account_id = None
        self.api_type = None
        self.name = None
        self.uh_x_modhash_header = None