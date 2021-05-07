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
        self.event_end = None
        self.event_start = None
        self.event_tz = None

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
        if self.event_end != None:
            body['event_end'] = self.event_end
        if self.event_start != None:
            body['event_start'] = self.event_start
        if self.event_tz != None:
            body['event_tz'] = self.event_tz
        return body


    def reset_queries(self):
        self.api_type = None
        self.return_rtjson = None
        self.richtext_json = None
        self.text = None
        self.thing_id = None
        self.id = None
        self.uh_x_modhash_header = None
