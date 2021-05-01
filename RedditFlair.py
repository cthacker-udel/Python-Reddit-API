from RedditClient import RedditClient

class RedditFlair(RedditClient):

    def __init__(self):
        super().__init__()
        self.flair_type = None
        self.uh_x_modhash = None
        self.subreddit_name = None
        self.flair_name = None


    def generate_body(self):
        body = {'api_type' : 'json'}
        if self.flair_type != None:
            body['flair_type'] = self.flair_type
        if self.uh_x_modhash != None:
            body['uh / X-Modhash header'] = self.uh_x_modhash
        if self.flair_name != None:
            body['name'] = self.flair_name
        return body


    def delete_body(self):

        self.flair_type = None
        self.uh_x_modhash = None
        self.flair_name = None