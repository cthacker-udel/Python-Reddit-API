from RedditClient import RedditClient

class RedditModmail(RedditClient):

    def __init__(self):
        super().__init__()
        self.entity = None
        self.state = None
        self.after = None
        self.limit = None
        self.sort = None
        self.subreddit = None
        self.body = None
        self.isAuthorHidden = None
        self.srName = None
        self.subject = None
        self.to = None
        self.conversation_id = None


    def generate_queries(self):
        body = {}

        if self.entity != None:
            body['entity'] = self.entity
        if self.state != None:
            body['state'] = self.state
        if self.after != None:
            body['after'] = self.after
        if self.limit != None:
            body['limit'] = self.limit
        if self.sort != None:
            body['sort'] = self.sort
        if self.body != None:
            body['body'] = self.body
        if self.isAuthorHidden != None:
            body['isAuthorHidden'] = self.isAuthorHidden
        if self.srName != None:
            body['srName'] = self.srName
        if self.subject != None:
            body['subject'] = self.subject
        if self.to != None:
            body['to'] = self.to


    def clear_queries(self):
        self.entity = None
        self.state = None
        self.after = None
        self.limit = None
        self.sort = None
        self.body = None
        self.isAuthorHidden = None
        self.srName = None
        self.subject = None
        self.to = None

    def get_subreddit(self):
        return self.subreddit