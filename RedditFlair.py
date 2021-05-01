from RedditClient import RedditClient

class RedditFlair(RedditClient):

    def __init__(self):
        super().__init__()
        self.flair_type = None
        self.uh_x_modhash = None
        self.subreddit_name = None
        self.flair_name = None
        self.css_class = None
        self.link = None
        self.user_name = None
        self.text = None
        self.flair_enabled = None
        self.flair_position = None
        self.flair_self_assign_enabled = None
        self.link_flair_position = None
        self.link_flair_self_assign_enabled = None


    def generate_body(self):
        body = {'api_type' : 'json'}
        if self.flair_type != None:
            body['flair_type'] = self.flair_type
        if self.uh_x_modhash != None:
            body['uh / X-Modhash header'] = self.uh_x_modhash
        if self.flair_name != None:
            body['name'] = self.flair_name
        if self.css_class != None:
            body['css_class'] = self.css_class
        if self.link != None:
            body['link'] = self.link
        if self.user_name != None:
            body['name'] = self.user_name
        if self.text != None:
            body['text'] = self.text
        if self.flair_enabled != None:
            body['flair_enabled'] = self.flair_enabled
        if self.flair_position != None:
            body['flair_position'] = self.flair_position
        if self.flair_self_assign_enabled != None:
            body['flair_self_assign_enabled'] = self.link_flair_self_assign_enabled
        if self.link_flair_position != None:
            body['link_flair_position'] = self.link_flair_position
        if self.link_flair_self_assign_enabled != None:
            body['link_flair_self_assign_enabled'] = self.link_flair_self_assign_enabled
        return body


    def delete_body(self):

        self.flair_type = None
        self.uh_x_modhash = None
        self.flair_name = None
        self.css_class = None
        self.link = None
        self.user_name = None
        self.text = None
        self.flair_enabled = None
        self.flair_position = None
        self.flair_self_assign_enabled = None
        self.link_flair_position = None
        self.link_flair_self_assign_enabled = None