from RedditClient import RedditClient


class PreferenceSettings(RedditClient):

    def __init__(self):
        super().__init__()
        self.accept_pms = None
        self.activity_relevant_ads = None
        self.allow_clicktracking = None
        self.beta = None
        self.clickgadget = None
        self.collapse_read_messages = None
        self.compress = None
        self.credit_autorenew = None
        self.default_comment_sort = None
        self.domain_details = None
        self.comment_reply = None
        self.email_chat_requests = None
        self.email_comment_reply = None
        self.email_digests = None
        self.email_messages = None
        self.email_post_reply = None
        self.email_private_message = None
        self.email_unsubscribe_all = None
        self.email_upvote_comment = None
        self.email_upvote_post = None
        self.email_user_new_follow = None
        self.email_username_mention = None
        self.enable_default_themes = None
        self.feed_recommendations_enabled = None
        self.g = None
        self.hide_ads = None
        self.hide_downs = None
        self.hide_from_robots = None
        self.hide_ups = None
        self.highlight_controversial = None
        self.highlight_new_comments = None
        self.ignore_suggested_sort = None
        self.in_redesign_beta = None
        self.label_nsfw = None
        self.lang = None
        self.legacy_search = None
        self.live_orangereds = None
        self.mark_messages_read = None
        self.media = None
        self.media_preview = None
        self.min_comment_score = 10
        self.min_link_score = 10
        self.monitor_mentions = None
        self.newwindow = None
        self.nightmode = None
        self.no_profanity = None
        self.num_comments = 10
        self.numsites = 10
        self.organic = None
        self.other_theme = None
        self.over_18 = None
        self.private_feeds = None
        self.profile_opt_out = None
        self.public_votes = None
        self.research = None
        self.search_include_over_18 = None
        self.send_crossport_messages = None
        self.send_welcome_messages = None
        self.show_flair = None
        self.show_gold_expiration = None
        self.show_link_flair = None
        self.show_location_based_recommendations = None
        self.show_presence = None
        self.show_promote = None
        self.show_stylesheets = None
        self.show_trending = None
        self.show_twitter = None
        self.store_visits = None
        self.survey_last_seen_time = None
        self.theme_selector = None
        self.third_party_data_personalized_ads = None
        self.third_party_personalized_ads = None
        self.third_party_site_data_personalized_ads = None
        self.third_party_site_data_personalized_content = None
        self.threaded_messages = None
        self.threaded_modmail = None
        self.top_karma_subreddits = None
        self.use_global_defaults = None
        self.video_autoplay = None
        self.where = None

    def convert_patch_body(self):
        body = {}
        if self.accept_pms != None and type(self.accept_pms) == str:
            body['accept_pms'] = self.accept_pms
        if self.activity_relevant_ads != None and type(self.activity_relevant_ads) == bool:
            body['activity_relevant_ads'] = self.activity_relevant_ads
        if self.allow_clicktracking != None and type(self.allow_clicktracking) == bool:
            body['allow_clicktracking'] = self.allow_clicktracking
        if self.beta != None and type(self.beta) == bool:
            body['beta'] = self.beta
        if self.clickgadget != None and type(self.clickgadget) == bool:
            body['clickgadget'] = self.clickgadget
        if self.collapse_read_messages != None and type(self.collapse_read_messages) == bool:
            body['collapse_read_messages'] = self.collapse_read_messages
        if self.compress != None and type(self.compress) == bool:
            body['compress'] = self.compress
        if self.credit_autorenew != None and type(self.credit_autorenew) == bool:
            body['credit_autorenew'] = self.credit_autorenew
        if self.default_comment_sort != None and type(self.default_comment_sort) == str:
            body['default_comment_sort'] = self.default_comment_sort
        if self.domain_details != None and type(self.domain_details) == bool:
            body['domain_details'] = self.domain_details
        if self.email_chat_requests != None and type(self.email_chat_requests) == bool:
            body['email_chat_requests'] = self.email_chat_requests
        if self.email_comment_reply != None and type(self.email_comment_reply) == bool:
            body['email_comment_reply'] = self.email_comment_reply
        if self.email_digests != None and type(self.email_digests) == bool:
            body['email_digests'] = self.email_digests
        if self.email_messages != None and type(self.email_messages) == bool:
            body['email_messages'] = self.email_messages
        if self.email_post_reply != None and type(self.email_post_reply) == bool:
            body['email_post_reply'] = self.email_post_reply
        if self.email_private_message != None and type(self.email_private_message) == bool:
            body['email_private_message'] = self.email_private_message
        if self.email_unsubscribe_all != None and type(self.email_unsubscribe_all) == bool:
            body['email_unsubscribe_all'] = self.email_unsubscribe_all
        if self.email_upvote_comment != None and type(self.email_upvote_comment) == bool:
            body['email_upvote_comment'] = self.email_upvote_comment
        if self.email_upvote_post != None and type(self.email_upvote_post) == bool:
            body['email_upvote_post'] = self.email_upvote_post
        if self.email_user_new_follow != None and type(self.email_user_new_follow) == bool:
            body['email_user_new_follower'] = self.email_user_new_follow
        if self.email_username_mention != None and type(self.email_username_mention) == bool:
            body['email_username_mention'] = self.email_username_mention
        if self.enable_default_themes != None and type(self.enable_default_themes) == bool:
            body['enable_default_themes'] = self.enable_default_themes
        if self.feed_recommendations_enabled != None and type(self.feed_recommendations_enabled) == bool:
            body['feed_recommendations_enabled'] = self.feed_recommendations_enabled
        if self.g != None and type(self.g) == str:
            body['g'] = self.g
        if self.hide_ads != None and type(self.hide_ads) == bool:
            body['hide_ads'] = self.hide_ads
        if self.hide_downs != None and type(self.hide_downs) == bool:
            body['hide_downs'] = self.hide_downs
        if self.hide_from_robots != None and type(self.hide_from_robots) == bool:
            body['hide_from_robots'] = self.hide_from_robots
        if self.hide_ups != None and type(self.hide_ups) == bool:
            body['hide_ups'] = self.hide_ups
        if self.highlight_controversial != None and type(self.highlight_controversial) == bool:
            body['highlight_controversial'] = self.highlight_controversial
        if self.highlight_new_comments != None and type(self.highlight_new_comments) == bool:
            body['highlight_new_comments'] = self.highlight_new_comments
        if self.ignore_suggested_sort != None and type(self.ignore_suggested_sort) == bool:
            body['ignore_suggested_sort'] = self.ignore_suggested_sort
        if self.in_redesign_beta != None and type(self.in_redesign_beta) == bool:
            body['in_redesign_beta'] = self.in_redesign_beta
        if self.label_nsfw != None and type(self.label_nsfw) == bool:
            body['label_nsfw'] = self.label_nsfw
        if self.lang != None and type(self.lang) == str:
            body['lang'] = self.lang
        if self.legacy_search != None and type(self.legacy_search) == bool:
            body['legacy_search'] = self.legacy_search
        if self.live_orangereds != None and type(self.live_orangereds) == bool:
            body['live_orangereds'] = self.live_orangereds
        if self.mark_messages_read != None and type(self.mark_messages_read) == bool:
            body['mark_messages_read'] = self.mark_messages_read
        if self.media != None and type(self.media) == str:
            body['media'] = self.media
        if self.media_preview != None and type(self.media_preview) == str:
            body['media_preview'] = self.media_preview
        if self.min_comment_score != None and type(self.min_comment_score) == int:
            body['min_comment_score'] = self.min_comment_score
        if self.min_link_score != None and type(self.min_link_score) == int:
            body['min_link_score'] = self.min_link_score
        if self.monitor_mentions != None and type(self.monitor_mentions) == bool:
            body['monitor_mentions'] = self.monitor_mentions
        if self.newwindow != None and type(self.newwindow) == bool:
            body['newwindow'] = self.newwindow
        if self.nightmode != None and type(self.nightmode) == bool:
            body['nightmode'] = self.nightmode
        if self.no_profanity != None and type(self.no_profanity) == bool:
            body['no_profanity'] = self.no_profanity
        if self.num_comments != None and type(self.num_comments) == int:
            body['num_comments'] = self.num_comments
        if self.numsites != None and type(self.numsites) == int:
            body['numsites'] = self.numsites
        if self.organic != None and type(self.organic) == bool:
            body['organic'] = self.organic
        if self.other_theme != None and type(self.other_theme) == str:
            body['other_theme'] = self.other_theme
        if self.over_18 != None and type(self.over_18) == str:
            body['over_18'] = self.over_18
        if self.private_feeds != None and type(self.private_feeds) == bool:
            body['private_feeds'] = self.private_feeds
        if self.profile_opt_out != None and type(self.profile_opt_out) == bool:
            body['profile_opt_out'] = self.profile_opt_out
        if self.public_votes != None and type(self.public_votes) == bool:
            body['public_votes'] = self.public_votes
        if self.research != None and type(self.research) == bool:
            body['research'] = self.research
        if self.search_include_over_18 != None and type(self.search_include_over_18) == bool:
            body['search_include_over_18'] = self.search_include_over_18
        if self.send_crossport_messages != None and type(self.send_crossport_messages) == bool:
            body['send_crossport_messages'] = self.send_crossport_messages
        if self.send_welcome_messages != None and type(self.send_welcome_messages) == bool:
            body['send_welcome_messages'] = self.send_welcome_messages
        if self.show_flair != None and type(self.show_flair) == bool:
            body['show_flair'] = self.show_flair
        if self.show_gold_expiration != None and type(self.show_gold_expiration) == bool:
            body['show_gold_expiration'] = self.show_gold_expiration
        if self.show_link_flair != None and type(self.show_link_flair) == bool:
            body['show_link_flair'] = self.show_link_flair
        if self.show_location_based_recommendations != None and type(self.show_location_based_recommendations) == bool:
            body['show_location_base_recommendations'] = self.show_location_based_recommendations
        if self.show_presence != None and type(self.show_presence) == bool:
            body['show_presence'] = self.show_presence
        if self.show_promote != None and type(self.show_promote) == bool:
            body['show_promote'] = self.show_promote
        if self.show_stylesheets != None and type(self.show_stylesheets) == bool:
            body['show_stylesheets'] = self.show_stylesheets
        if self.show_trending != None and type(self.show_trending) == bool:
            body['show_trending'] = self.show_trending
        if self.show_twitter != None and type(self.show_twitter) == bool:
            body['show_twitter'] = self.show_twitter
        if self.store_visits != None and type(self.store_visits) == bool:
            body['store_visits'] = self.store_visits
        if self.survey_last_seen_time != None and type(self.survey_last_seen_time) == int:
            body['survey_last_seen_time'] = self.survey_last_seen_time
        if self.theme_selector != None and type(self.theme_selector) == str:
            body['theme_selector'] = self.theme_selector
        if self.third_party_data_personalized_ads != None and type(self.third_party_data_personalized_ads) == bool:
            body['third_party_data_personalized_ads'] = self.third_party_data_personalized_ads
        if self.third_party_personalized_ads != None and type(self.third_party_personalized_ads) == bool:
            body['third_party_personalized_ads'] = self.third_party_data_personalized_ads
        if self.third_party_site_data_personalized_ads != None and type(
                self.third_party_site_data_personalized_ads) == bool:
            body['third_party_site_data_personalized_ads'] = self.third_party_site_data_personalized_ads
        if self.third_party_site_data_personalized_content != None and type(
                self.third_party_site_data_personalized_content) == bool:
            body['third_party_site_data_personalized_content'] = self.third_party_site_data_personalized_content
        if self.threaded_messages != None and type(self.threaded_messages) == bool:
            body['threaded_messages'] = self.threaded_messages
        if self.threaded_modmail != None and type(self.threaded_modmail) == bool:
            body['threaded_modmail'] = self.threaded_modmail
        if self.top_karma_subreddits != None and type(self.top_karma_subreddits) == bool:
            body['top_karma_subreddits'] = self.top_karma_subreddits
        if self.use_global_defaults != None and type(self.use_global_defaults) == bool:
            body['use_global_defaults'] = self.use_global_defaults
        if self.video_autoplay != None and type(self.video_autoplay) == bool:
            body['video_autoplay'] = self.video_autoplay
        return body
