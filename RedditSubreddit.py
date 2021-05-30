from RedditClient import RedditClient

class RedditSubreddit(RedditClient):

    def __init__(self):
        self.where = None
        self.subreddit = None

        self.after = None
        self.before = None
        self.count = None
        self.limit = None
        self.show = None
        self.sr_detail = None
        self.user = None
        self.uh_x_modhash_header = None
        self.api_type = 'json'
        self.img_name = None
        self.omit = None
        self.over_18 = None
        self.srnames = None
        self.include_over_18 = None
        self.include_unadvertisable = None
        self.query = None
        self.search_query_id = None
        self.typehead_active = None
        self.exact = None


    def generate_queries(self):

        body = {}

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
        if self.user != None:
            body['user'] = self.user
        if self.uh_x_modhash_header != None:
            body['uh / X-Modhash header'] = self.uh_x_modhash_header
        if self.api_type != None:
            body['api_type'] = self.api_type
        if self.img_name != None:
            body['img_name'] = self.img_name
        if self.omit != None:
            body['omit'] = self.omit
        if self.over_18 != None:
            body['over_18'] = self.over_18
        if self.srnames != None:
            body['srnames'] = self.srnames
        if self.exact != None:
            body['exact'] = self.exact
        if self.include_over_18 != None:
            body['include_over_18'] = self.include_over_18
        if self.include_unadvertisable != None:
            body['include_unadvertisable'] = self.include_unadvertisable
        if self.query != None:
            body['query'] = self.query
        if self.search_query_id != None:
            body['search_query'] = self.search_query_id
        if self.typehead_active != None:
            body['typehead_active'] = self.typehead_active
        return body


    def clear_queries(self):

        self.after = None
        self.before = None
        self.count = None
        self.limit = None
        self.show = None
        self.sr_detail = None
        self.user = None
        self.uh_x_modhash_header = None
        self.api_type = 'json'
        self.img_name = None
        self.omit = None
        self.over_18 = None
        self.srnames = None
        self.include_over_18 = None
        self.include_unadvertisable = None
        self.query = None
        self.search_query_id = None
        self.typehead_active = None
        self.exact = None