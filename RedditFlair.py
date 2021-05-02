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
        self.flair_csv = []
        self.after = None
        self.before = None
        self.count = None
        self.limit = None
        self.show = None
        self.sr_detail = None
        self.is_newlink = None
        self.flair_template_id = None
        self.text_editable = None
        self.allowable_content = None
        self.background_color = None
        self.max_emojis = None
        self.mod_only = None
        self.override_css = None
        self.text_color = None
        self.return_rtson = None


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
        if len(self.flair_csv) > 0:
            body['flair_csv'] = ','.join(self.flair_csv)
        if self.after != None:
            body['after'] = self.after
        if self.before != None:
            body['before'] = self.before
        if self.count != None:
            body['count'] = self.count
        if self.limit != None:
            body['limit'] = self.limit
        if self.show != None:
            body['show'] = self.show
        if self.sr_detail != None:
            body['sr_detail'] = self.sr_detail
        if self.is_newlink != None:
            body['is_newlink'] = self.is_newlink
        if self.flair_template_id != None:
            body['flair_template_id'] = self.flair_template_id
        if self.text_editable != None:
            body['text_editable'] = self.text_editable
        if self.allowable_content != None:
            body['allowable_content']  = self.allowable_content
        if self.background_color != None:
            body['background_color'] = self.background_color
        if self.max_emojis != None:
            body['max_emojis'] = self.max_emojis
        if self.mod_only != None:
            body['mod_only'] = self.mod_only
        if self.override_css != None:
            body['override_css'] = self.override_css
        if self.text_color != None:
            body['text_color'] = self.text_color
        if self.return_rtson != None:
            body['return_rtson'] = self.return_rtson
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
        self.flair_csv = []
        self.after = None
        self.before = None
        self.count = None
        self.limit = None
        self.show = None
        self.sr_detail = None
        self.is_newlink = None
        self.flair_template_id = None
        self.text_editable = None
        self.allowable_content = None
        self.background_color = None
        self.max_emojis = None
        self.mod_only = None
        self.override_css = None
        self.text_color = None
        self.return_rtson = None
