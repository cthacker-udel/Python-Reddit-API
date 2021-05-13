from RedditClient import RedditClient


class RedditListing(RedditClient):

    def __init__(self):
        super().__init__()
        self.after = None
        self.before = None
        self.count = None
        self.limit = None
        self.show = None
        self.sr_detail = None
        self.names = []
        self.subreddit_name = None
        self.article = None
        self.comment = None
        self.context = None
        self.depth = None
        self.limit = None
        self.showedits = None
        self.showmedia = None
        self.showmore = None
        self.showtitle = None
        self.sort = None
        self.theme = None
        self.threaded = None
        self.truncate = None
        self.crossposts_only = None
        self.sr = None
        self.t = None



    def generate_queries(self):
        body = []
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
        if len(self.names) > 0:
            body['names'] = ','.join(self.names)
        if self.article != None:
            body['article'] = self.article
        if self.comment != None:
            body['comment'] = self.comment
        if self.context != None:
            body['depth'] = self.depth
        if self.limit != None:
            body['limit'] = self.limit
        if self.showedits != None:
            body['showedits'] = self.showedits
        if self.showmedia != None:
            body['showmedia'] = self.showmedia
        if self.showmore != None:
            body['showmore'] = self.showmore
        if self.showtitle != None:
            body['showtitle'] = self.showtitle
        if self.sort != None:
            body['sort'] = self.sort
        if self.theme != None:
            body['theme'] = self.theme
        if self.threaded != None:
            body['threaded'] = self.threaded
        if self.truncate != None:
            body['truncate'] = self.truncate
        if self.crossposts_only != None:
            body['crossports_only'] = self.crossposts_only
        if self.sr != None:
            body['sr'] = self.sr
        if self.t != None:
            body['t'] = self.t
        return body

    def clear_queries(self):
        self.after = None
        self.before = None
        self.count = None
        self.limit = None
        self.show = None
        self.sr_detail = None
        self.names = []
        self.article = None
        self.comment = None
        self.context = None
        self.depth = None
        self.limit = None
        self.showedits = None
        self.showmedia = None
        self.showmore = None
        self.showtitle = None
        self.sort = None
        self.theme = None
        self.threaded = None
        self.truncate = None
        self.crossposts_only = None
        self.sr = None
        self.t = None


    def get_subreddit_name(self):
        return self.subreddit_name