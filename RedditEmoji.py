from RedditClient import RedditClient

class RedditEmoji(RedditClient):

    def __init__(self):
        super().__init__()
        self.mod_flair_only = None
        self.name = None
        self.post_flair_allowed = None
        self.s3_key = None
        self.user_flair_allowed = None
        self.subreddit_name = None


    def generate_body(self):
        body = {}
        if self.mod_flair_only != None:
            body['mod_flair_only'] = self.mod_flair_only
        if self.name != None:
            body['name'] = self.name
        if self.post_flair_allowed != None:
            body['post_flair_allowed'] = self.post_flair_allowed
        if self.s3_key != None:
            body['s3_key'] = self.s3_key
        if self.user_flair_allowed != None:
            body['user_flair_allowed'] = self.user_flair_allowed

    def erase_body(self):

        self.mod_flair_only = None
        self.name = None
        self.post_flair_allowed = None
        self.s3_key = None
        self.user_flair_allowed = None