from RedditClient import RedditClient

class RedditPrivate(RedditClient):

    def __init__(self):
        super().__init__()
        self.id = None
        self.uh_x_modhash_header = None
        self.api_type = 'json'
        self.from_sr = None
        self.g_recaptcha_response = None
        self.subject = None
        self.text = None
        self.to = None

    def generate_queries(self):
        body = {}
        if self.id != None:
            body['id'] = self.id
        if self.uh_x_modhash_header != None:
            body['uh / X-Modhash header'] = self.uh_x_modhash_header
        if self.api_type != None:
            body['api_type'] = self.api_type
        if self.from_sr != None:
            body['from_sr'] = self.from_sr
        if self.g_recaptcha_response != None:
            body['g-recaptcha-response'] = self.g_recaptcha_response
        if self.subject != None:
            body['subject'] = self.subject
        if self.text != None:
            body['text'] = self.text
        if self.to != None:
            body['to'] = self.to
        return body