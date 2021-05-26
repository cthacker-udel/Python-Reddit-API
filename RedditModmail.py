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
        self.isInternal = None
        self.duration = None
        self.conversation_ids = []


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
        if self.isInternal != None:
            body['isInternal'] = self.isInternal
        if self.duration != None:
            body['duration'] = self.duration
        if len(self.conversation_ids) > 0:
            body['conversationIds'] = ','.join(self.conversation_ids)
        return body


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
        self.isInternal = None

    def get_subreddit(self):
        return self.subreddit

