from RedditClient import RedditClient

class RedditGold(RedditClient):

    def __init__(self):
        super().__init__()
        self.full_name = None
        self.months = None
        self.username = None


    def generate_body(self):
        body = {}
        if self.full_name != None:
            body['fullname'] = self.full_name
        if self.months != None:
            body['months'] = self.months
        if self.username != None:
            body['username'] = self.username
        return body


    def delete_body(self):
        self.full_name = None
        self.months = None
        self.username = None