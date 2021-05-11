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
        self.follow = None
        self.fullname = None
        self.sr_name = None
        self.children = None
        self.depth = None
        self.limit_children = None
        self.link_id = None
        self.sort = None
        self.custom_text = None
        self.from_help_desk = None
        self.from_modmail = None
        self.modmail_conv_id = None
        self.other_reason = None
        self.reason = None
        self.rule_reason = None
        self.site_reason = None
        self.usernames = None
        self.award_id = None
        self.category = None
        self.state = None
        self.num = None
        self.to_profile = None

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
        if self.follow != None:
            body['follow'] = self.follow
        if self.fullname != None:
            body['fullname'] = self.fullname
        if self.sr_name != None:
            body['sr_name'] = self.sr_name
        if self.children != None:
            body['children'] = self.children
        if self.depth != None:
            body['depth'] = self.depth
        if self.limit_children != None:
            body['limit_children'] = self.limit_children
        if self.link_id != None:
            body['link_id'] = self.link_id
        if self.sort != None:
            body['sort'] = self.sort
        if self.custom_text != None:
            body['custom_text'] = self.custom_text
        if self.from_help_desk != None:
            body['from_help_desk'] = self.from_help_desk
        if self.from_modmail != None:
            body['from_modmail'] = self.from_modmail
        if self.modmail_conv_id != None:
            body['modmail_conv_id'] = self.modmail_conv_id
        if self.other_reason != None:
            body['other_reason'] = self.other_reason
        if self.reason != None:
            body['reason'] = self.reason
        if self.rule_reason != None:
            body['rule_reason'] = self.rule_reason
        if self.site_reason != None:
            body['site_reason'] = self.reason
        if self.thing_id != None:
            body['thing_id'] = self.thing_id
        if self.usernames != None:
            body['usernames'] = self.usernames
        if self.award_id != None:
            body['award_id'] = self.award_id
        if self.category != None:
            body['category'] = self.category
        if self.state != None:
            body['state'] = self.state
        if self.num != None:
            body['num'] = self.num
        if self.to_profile != None:
            body['to_profile'] = self.to_profile
        return body


    def reset_queries(self):
        self.api_type = None
        self.return_rtjson = None
        self.richtext_json = None
        self.text = None
        self.thing_id = None
        self.id = None
        self.uh_x_modhash_header = None
        self.follow = None
        self.fullname = None
        self.children = None
        self.depth = None
        self.limit_children = None
        self.link_id = None
        self.sort = None
        self.custom_text = None
        self.from_help_desk = None
        self.from_modmail = None
        self.modmail_conv_id = None
        self.other_reason = None
        self.reason = None
        self.rule_reason = None
        self.site_reason = None
        self.usernames = None
        self.award_id = None
        self.category = None
        self.state = None
        self.num = None
        self.to_profile = None
