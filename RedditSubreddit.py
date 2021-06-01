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

        self.admin_override_spam_comments = None
        self.admin_override_spam_links = None
        self.admin_override_spam_selfports = None
        self.all_original_content = None
        self.allow_chat_post_creation = None
        self.allow_discovery = None
        self.allow_galleries = None
        self.allow_images = None
        self.allow_polls = None
        self.allow_post_crossposts = None
        self.allow_predictions = None
        self.allow_predictions_tournaments = None
        self.allow_top = None
        self.allow_videos = None
        self.api_type = None
        self.automated_reporting_level_abuse = None
        self.automated_reporting_level_hate = None
        self.collapse_deleted_comments = None
        self.comment_score_hide_mins = None
        self.crowd_control_chat_level = None
        self.crowd_control_level = None
        self.crowd_control_mode = None
        self.description = None
        self.disable_contributor_requests = None
        self.exclude_banned_modqueue = None
        self.free_form_reports = None
        self.g_recaptcha_response = None
        self.header_title = None
        self.hide_ads = None
        self.key_color = None
        self.lang = None
        self.link_type = None
        self.name = None
        self.new_pinned_post_pns_enabled = None
        self.original_content_tag_enabled = None
        self.over_18 = None
        self.prediction_leaderboard_entry_type = None
        self.public_description = None
        self.restrict_commenting = None
        self.show_media = None
        self.show_media_preview = None
        self.spam_comments = None
        self.spam_links = None
        self.spam_selfposts = None
        self.spoilers_enabled = None
        self.sr = None
        self.submit_link_label = None
        self.submit_text = None
        self.submit_text_label = None
        self.suggested_comment_sort = None
        self.title = None
        self.toxicity_threshold_chat_level = None
        self.type =  None
        self.user_flair_pns_enabled = None
        self.welcome_message_enabled = None
        self.welcome_message_text = None
        self.wiki_edit_age = None
        self.wiki_edit_karma = None
        self.wikimode = N


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