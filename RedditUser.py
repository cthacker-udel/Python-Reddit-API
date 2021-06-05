from RedditClient import RedditClient

class RedditUser(RedditClient):


    def __init__(self):
        self.account_id = None
        self.api_type = None
        self.name = None
        self.uh_x_modhash_header = None
        self.subreddit = None

        self.ban_context = None
        self.ban_message = None
        self.ban_reason = None
        self.container = None
        self.duration = None
        self.note = None
        self.permissions = None
        self.type = None


    def generate_queries(self):
        body = {}
        if self.ban_context != None:
            body['ban_context'] = self.ban_context
        if self.ban_message != None:
            body['ban_message'] = self.ban_message
        if self.ban_reason != None:
            body['ban_reason'] = self.ban_reason
        if self.container != None:
            body['container'] = self.container
        if self.duration != None:
            body['duration'] = self.duration
        if self.note != None:
            body['note'] = self.note
        if self.permissions != None:
            body['permissions'] = self.permissions
        if self.type != None:
            body['type'] = self.type
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
        self.ban_context = None
        self.ban_message = None
        self.ban_reason = None
        self.container = None
        self.duration = None
        self.note = None
        self.permissions = None
        self.type = None