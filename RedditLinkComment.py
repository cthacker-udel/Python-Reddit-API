from RedditClient import RedditClient


class RedditLinkComment(RedditClient):

    def __init__(self):
        super().__init__()
        self.api_type = None
        self.return_rtjson = None
        self.richtext_json = None
        self.text = None
        self.thing_id = None
        self.id = None
        self.uh_x_modhash_header = None

    def generate_body(self):
        body = {}
        if self.api_type != None:
            body['api_type'] = self.api_type
        if self.return_rtjson != None:
            body['return_rtjson'] = self.return_rtjson
        if self.richtext_json != None:
            body['richtext_json'] = self.richtext_json
        if self.text != None:
            body['text'] = self.text
        if self.thing_id != None:
            body['thing_id'] = self.thing_id
        if self.uh_x_modhash_header != None:
            body['uh / X-Modhash header'] = self.uh_x_modhash_header
        return body


    def reset_queries(self):
        self.api_type = None
        self.return_rtjson = None
        self.richtext_json = None
        self.text = None
        self.thing_id = None
        self.id = None
        self.uh_x_modhash_header = None
