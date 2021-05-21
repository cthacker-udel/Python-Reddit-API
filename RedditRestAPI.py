import requests
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import DriverManager as FirefoxDriverManager
from webdriver_manager.logger import log
from pprint import pprint
import time

from RedditClient import RedditClient

base_auth_url = 'https://www.reddit.com/api/v1/authorize'

# base_url = 'https://www.reddit.com'

# base_url = 'https://ssl.reddit.com'

base_url = 'https://oauth.reddit.com'


def get_auth_header(redditclient):
    headers = {'Authorization': 'Bearer {}'.format(redditclient.access_token),
               'User-Agent': 'cthacker-udel Reddit API Python Wrapper'}

    return headers


def implicit_grant_flow(redditclient):
    try:
        br = webdriver.Firefox(FirefoxDriverManager().install())
    except Exception as e:
        try:
            br = webdriver.Chrome(ChromeDriverManager().install())
        except Exception as e:
            return None

    queryStringList = []

    params = {'redditclient_id': redditclient.redditclient_id,
              'response_type': 'token',
              'state': 'RANDOM_STRING',
              'redirect_uri': redditclient.redirect_uri,
              'scope': ' '.join(redditclient.scopes)}

    for eachkey in params.keys():
        queryStringList.append('{}={}'.format(eachkey, params[eachkey]))

    queryString = '&'.join(queryStringList)

    url = base_auth_url + '?' + queryString
    print(url)

    br.get(url)

    ### find login box

    log('Filling in username')

    username_box = br.find_element_by_id('loginUsername')
    username_box.send_keys(redditclient.username)

    time.sleep(1)

    log('Filling in password')

    password_box = br.find_element_by_id('loginPassword')
    password_box.send_keys(redditclient.password)

    time.sleep(2)

    login_button = br.find_element_by_xpath('/html/body/div/main/div[1]/div/div[2]/form/fieldset[5]/button').click()

    time.sleep(4)

    log('Allowing Python-Wrapper Reddit API permission')

    allow_button = br.find_element_by_xpath('/html/body/div[3]/div/div[2]/form/div/input[1]').click()

    time.sleep(3)

    log('Acquiring code to generate token')

    curr_url = br.current_url

    response = curr_url.split('&token_type')

    redditclient.set_access_token(response[0].split("access_token=")[1])

    return response


def token_post_request(redditclient):
    url = base_url + '/api/v1/access_token'

    user_agent = {'User-Agent': 'cthacker-udel Reddit API Python Wrapper'}

    redditclient_auth = requests.auth.HTTPBasicAuth(redditclient.redditclient_id, redditclient.redditclient_secret)

    headers = {'User-Agent': 'cthacker-udel Reddit API Python Wrapper'}

    data = {'grant_type': 'authorization_code',
            'code': redditclient.oauth_code,
            'redirect_uri': redditclient.redirect_uri}

    request = requests.post(url, data=data, headers=headers, auth=redditclient_auth)

    pprint(request)


############################################
#       Account Methods
############################################


def get_user_identitiy(redditclient):
    url = base_url + '/api/v1/me'

    headers = get_auth_header(redditclient)

    # redditclient_auth = requests.auth.HTTPBasicAuth(redditclient.redditclient_id, redditclient.redditclient_secret)

    request = requests.get(url, headers=headers).json()

    pprint(request)

    print('\n\n')

    return request


def get_user_identity_features(redditclient):
    identity = get_user_identitiy(redditclient)

    return identity['features']


def get_user_identity_attribute(redditclient, attribute):
    identity = get_user_identitiy(redditclient)

    return identity[attribute]


def get_user_karma(redditclient):
    url = base_url + '/api/v1/me/karma'

    headers = get_auth_header(redditclient)

    request = requests.get(url, headers=headers).json()

    pprint(request)

    return request.status_code == 200


def get_user_preference_settings(redditclient):
    url = base_url + '/api/v1/me/prefs'

    headers = get_auth_header(redditclient)

    request = requests.get(url, headers=headers).json()

    pprint(request)

    return request.status_code == 200


def edit_user_preference_settings(redditclient):
    url = base_url + '/api/v1/me/prefs'

    headers = get_auth_header(redditclient)

    body = redditclient.PreferenceSettings.convert_patch_body()

    request = requests.patch(url, json=body, headers=headers)

    pprint(request)

    return request.status_code == 200


def get_user_trophies(redditclient):
    url = base_url + '/api/v1/me/trophies'

    headers = get_auth_header(redditclient)

    request = requests.get(url, headers=headers)

    pprint(request)

    return request.status_code == 200


def get_preference_settings_where(redditclient):
    url = base_url + '/prefs/{}'.format(redditclient.PreferenceSettings.where)

    headers = get_auth_header(redditclient)

    request = requests.get(url, headers=headers)

    pprint(request)

    return request.status_code == 200


def get_preference_settings_v1(redditclient):
    url = base_url + "/api/v1/me/{}".format(redditclient.PreferenceSettings.where)

    headers = get_auth_header(redditclient)

    request = requests.get(url, headers=headers)

    pprint(request)

    return request.status_code == 200


#################################
# Captcha Methods
#################################


def check_captcha(redditclient):
    url = base_url + "/api/needs_captcha"

    headers = get_auth_header(redditclient)

    request = requests.get(url, headers=headers)

    pprint(request)

    return request.status_code == 200


#################################
# Collections Methods
#################################


def add_post_to_collection(redditclient):
    url = base_url + '/api/v1/collections/add_post_to_collection'

    body = redditclient.RedditCollection.generate_body()

    headers = get_auth_header(redditclient)

    request = requests.post(url, headers=headers, body=body)

    pprint(request)

    return request.status_code == 200


def fetch_collection(redditclient):
    url = base_url + '/api/v1/collections/collection'

    body = redditclient.RedditCollection.generate_body()

    headers = get_auth_header(redditclient)

    request = requests.get(url, headers=headers, params=body)

    pprint(request)

    return request.status_code == 200


def create_collection(redditclient):
    url = base_url + '/api/v1/collections/create_collection'

    body = redditclient.RedditCollection.generate_body()

    headers = get_auth_header(redditclient)

    request = requests.post(url, headers=headers, body=body)

    pprint(request)

    return request.status_code == 200


def delete_collection(redditclient):
    url = base_url + '/api/v1/collections/delete_collection'

    body = redditclient.RedditCollection.generate_body()

    headers = get_auth_header(redditclient)

    request = requests.post(url, headers=headers, body=body)

    pprint(request)

    return request.status_code == 200


def follow_collection(redditclient):
    url = base_url + '/api/v1/collections/follow_collection'

    body = redditclient.RedditCollection.generate_body()

    headers = get_auth_header(redditclient)

    request = requests.post(url, headers=headers, body=body)

    pprint(request)

    return request.status_code == 200


def remove_post_in_collection(redditclient):
    url = base_url + '/api/v1/collections/remove_post_in_collection'

    body = redditclient.RedditCollection.generate_body()

    headers = get_auth_header(redditclient)

    request = requests.post(url, headers=headers, body=body)

    pprint(request)

    return request.status_code == 200


def reorder_collection(redditclient):
    url = base_url + '/api/v1/collections/reorder_collection'

    body = redditclient.RedditCollection.generate_body()

    headers = get_auth_header(redditclient)

    request = requests.post(url, headers=headers, body=body)

    pprint(request)

    return request.status_code == 200


def fetch_subreddit_collections(redditclient):
    url = base_url + '/api/v1/collections/subreddit_collections'

    body = redditclient.RedditCollection.generate_body()

    headers = get_auth_header(redditclient)

    request = requests.get(url, headers=headers, params=body)

    pprint(request)

    return request.status_code == 200


def update_collection_description(redditclient):
    url = base_url + '/api/v1/collections/update_collection_description'

    body = redditclient.RedditCollection.generate_body()

    headers = get_auth_header(redditclient)

    request = requests.post(url, headers=headers, body=body)

    pprint(request)

    return request.status_code == 200


def update_collection_display_layout(redditclient):
    url = base_url + '/api/v1/collections/update_collection_display_layout'

    body = redditclient.RedditCollection.generate_body()

    headers = get_auth_header(redditclient)

    request = requests.post(url, headers=headers, body=body)

    pprint(request)

    return request.status_code == 200


def update_collection_title(redditclient):
    url = base_url + '/api/v1/collections/update_collection_title'

    body = redditclient.RedditCollection.generate_body()

    headers = get_auth_header(redditclient)

    request = requests.post(url, headers=headers, body=body)

    pprint(request)

    return request.status_code == 200


#################################
# EMOJI METHODS
#################################


def add_emoji_to_subreddit(redditclient):
    url = base_url + '/api/v1/{}/emoji.json'.format(redditclient.RedditEmoji.subreddit_name)

    body = redditclient.RedditEmoji.generate_body()

    headers = get_auth_header(redditclient)

    request = requests.post(url, body=body, headers=headers)

    pprint(request)


def delete_subreddit_emoji(redditclient):
    url = base_url + '/api/v1/{}/emoji/{}'.format(redditclient.RedditEmoji.subreddit_name,
                                                  redditclient.RedditEmoji.name)

    headers = get_auth_header(redditclient)

    request = requests.delete(url, headers=headers)

    pprint(request)


def upload_emoji_asset(redditclient):
    url = base_url + '/api/v1/{}/emoji_asset_upload_s3.json'.format(redditclient.RedditEmoji.subreddit_name)

    headers = get_auth_header(redditclient)

    body = redditclient.RedditEmoji.generate_body()

    request = requests.post(url, headers=headers, body=body)

    pprint(request)


def set_emoji_size(redditclient):
    url = base_url + '/api/v1/{}/emoji_custom_size'.format(redditclient.RedditEmoji.subreddit_name)

    headers = get_auth_header(redditclient)

    body = redditclient.RedditEmoji.generate_body()

    request = requests.post(url, headers=headers, body=body)

    pprint(request)


def get_subreddit_emojis(redditclient):
    url = base_url + '/api/v1/{}/emojis/all'.format(redditclient.RedditEmoji.subreddit_name)

    headers = get_auth_header(redditclient)

    request = requests.get(url, headers=headers)

    pprint(request)


##############################
## FLAIR METHODS
##############################


def clear_flair_templates(redditclient):
    url = base_url + '[/r/{}]/api/clearflairtemplates'.format(redditclient.RedditFlair.subreddit_name)

    headers = get_auth_header(redditclient)

    data = redditclient.RedditFlair.generate_body()

    request = requests.post(url, headers=headers, body=data)

    pprint(request)


def delete_flair(redditclient):
    url = base_url + '[/r/{}]/api/deleteflair'.format(redditclient.RedditFlair.subreddit_name)

    headers = get_auth_header(redditclient)

    data = redditclient.RedditFlair.generate_body()

    request = requests.post(url, headers=headers, body=data)

    pprint(request)


def delete_flair_template(redditclient):
    url = base_url + '[/r/{}]/api/deleteflairtemplate'.format(redditclient.RedditFlair.subreddit_name)

    headers = get_auth_header(redditclient)

    data = redditclient.RedditFlair.generate_body()

    request = requests.post(url, headers=headers, body=data)

    pprint(request)


def get_flair(redditclient):
    url = base_url + '[/r/{}]/api/flair'.format(redditclient.RedditFlair.subreddit_name)

    headers = get_auth_header(redditclient)

    data = redditclient.RedditFlair.generate_body()

    request = requests.post(url, headers=headers, body=data)

    pprint(request)


def update_flair_template_order(redditclient):
    url = base_url + '[/r/{}]/api/flair_template_order'.format(redditclient.RedditFlair.subreddit_name)

    headers = get_auth_header(redditclient)

    data = redditclient.RedditFlair.generate_body()

    request = requests.patch(url, body=data, headers=headers)

    pprint(request)


def update_flair_config(redditclient):
    url = base_url + '[/r/{}]/api/flairconfig'.format(redditclient.RedditFlair.subreddit_name)

    headers = get_auth_header(redditclient)

    data = redditclient.RedditFlair.generate_body()

    request = requests.post(url, body=data, headers=headers)

    pprint(request)


def flair_config_users(redditclient):
    url = base_url + '[/r/{}]/api/flaircsv'.format(redditclient.RedditFlair.subreddit_name)

    headers = get_auth_header(redditclient)

    data = redditclient.RedditFlair.generate_body()

    request = requests.post(url, body=data, headers=headers)

    pprint(request)


def flair_list(redditclient):
    url = base_url + '[/r/{}]/api/flairlist'.format(redditclient.RedditFlair.subreddit_name)

    headers = get_auth_header(redditclient)

    data = redditclient.RedditFlair.generate_body()

    request = requests.get(url, headers=headers, params=data)

    pprint(request)


def flair_selector(redditclient):
    url = base_url + '[/r/{}]/api/flairselector'.format(redditclient.RedditFlair.subreddit_name)

    headers = get_auth_header(redditclient)

    data = redditclient.RedditFlair.generate_body()

    request = requests.post(url, headers=headers, body=data)

    pprint(request)


def flair_template(redditclient):
    url = base_url + '[/r/{}]/api/flairtemplate'.format(redditclient.RedditFlair.subreddit_name)

    headers = get_auth_header(redditclient)

    data = redditclient.RedditFlair.generate_body()

    request = requests.post(url, headers=headers, body=data)

    pprint(request)


def flair_template_v2(redditclient):
    url = base_url + '[/r/{}]/api/flairtemplate_v2'.format(redditclient.RedditFlair.subreddit_name)

    headers = get_auth_header(redditclient)

    data = redditclient.RedditFlair.generate_body()

    request = requests.post(url, headers=headers, body=data)

    pprint(request)


def link_flair(redditclient):
    url = base_url + '[/r/{}]/api/link_flair'.format(redditclient.RedditFlair.subreddit_name)

    headers = get_auth_header(redditclient)

    request = requests.get(url, headers=headers)

    pprint(request)


def link_flair_v2(redditclient):
    url = base_url + '[/r/{}]/api/link_flair_v2'.format(redditclient.RedditFlair.subreddit_name)

    headers = get_auth_header(redditclient)

    request = requests.get(url, headers=headers)

    pprint(request)


def select_flair(redditclient):
    url = base_url + '[/r/{}]/api/selectflair'.format(redditclient.RedditFlair.subreddit_name)

    headers = get_auth_header(redditclient)

    body = redditclient.RedditFlair.generate_body()

    request = requests.post(url, headers=headers, body=body)

    pprint(request)


def set_flair_enabled(redditclient):
    url = base_url + '[/r/{}]/api/setflairenabled'.format(redditclient.RedditFlair.subreddit_name)

    headers = get_auth_header(redditclient)

    body = redditclient.RedditFlair.generate_body()

    request = requests.post(url, headers=headers, body=body)

    pprint(request)


def user_flair(redditclient):
    url = base_url + '[/r/{}]/api/user_flair'.format(redditclient.RedditFlair.subreddit_name)

    headers = get_auth_header(redditclient)

    request = requests.get(url, headers=headers)

    pprint(request)


def user_flair_v2(redditclient):
    url = base_url + '[/r/{}]/api/user_flair_v2'.format(redditclient.RedditFlair.subreddit_name)

    headers = get_auth_header(redditclient)

    request = requests.get(url, headers=headers)

    pprint(request)


###############
# GOLD METHODS
###############


def gold_fullname(redditclient):
    url = base_url + '/api/v1/gold/gild/{}'.format(redditclient.RedditGold.full_name)

    headers = get_auth_header(redditclient)

    body = redditclient.RedditGold.generate_body()

    request = requests.post(url, headers=headers, body=body)

    pprint(request)


def gold_username(redditclient):
    url = base_url + '/api/v1/gold/give/{}'.format(redditclient.RedditGold.username)

    headers = get_auth_header(redditclient)

    body = redditclient.RedditGold.generate_body()

    request = requests.post(url, headers=headers, body=body)

    pprint(request)


###################
# LINKS & COMMENTS
###################

def submit_comment(redditclient):
    url = base_url + '/api/comment'

    headers = get_auth_header(redditclient)

    body = redditclient.RedditLinkComment.generate_body()

    request = requests.post(url, headers=headers, body=body)

    pprint(request)


def delete_link_or_comment(redditclient):
    url = base_url + '/api/del'

    headers = get_auth_header(redditclient)

    body = redditclient.RedditLinkComment.generate_body()

    request = requests.delete(url, headers=headers, body=body)

    pprint(request)


def edit_comment_text(redditclient):
    url = base_url + "/api/editusertext"

    headers = get_auth_header(redditclient)

    body = redditclient.RedditLinkComment.generate_body()

    request = requests.post(url, headers=headers, body=body)

    pprint(request)


def add_or_modify_event_times(redditclient):
    url = base_url + '/api/event_post_time'

    headers = get_auth_header(redditclient)

    body = redditclient.RedditLinkComment.generate_body()

    request = requests.post(url, headers=headers, body=body)

    pprint(request)


def follow_post(redditclient):
    url = base_url + '/api/follow_post'

    headers = get_auth_header(redditclient)

    body = redditclient.RedditLinkComment.generate_body()

    request = requests.post(url, headers=headers, body=body)

    pprint(request)


def hide_link(redditclient):
    url = base_url + '/api/hide'

    headers = get_auth_header(redditclient)

    body = redditclient.RedditLinkComment.generate_body()

    request = requests.post(url, headers=headers, body=body)

    pprint(request)


def comment_link_info(redditclient):
    url = base_url + '[/r/{}]/api/info'

    headers = get_auth_header(redditclient)

    body = redditclient.RedditLinkComment.generate_body()

    request = requests.get(url, headers=headers, params=body)

    pprint(request)


def lock_comment(redditclient):
    url = base_url + '/api/lock'

    headers = get_auth_header(redditclient)

    body = redditclient.RedditLinkComment.generate_body()

    request = requests.post(url, headers=headers, body=body)

    pprint(request)


def mark_link_nsfw(redditclient):
    url = base_url + '/api/marknsfw'

    headers = get_auth_header(redditclient)

    body = redditclient.RedditLinkComment.generate_body()

    request = requests.post(url, headers=headers, body=body)

    pprint(request)


def retrieve_additional_comments(redditclient):
    url = base_url + '/api/morechildren'

    headers = get_auth_header(redditclient)

    body = redditclient.RedditLinkComment.generate_body()

    request = requests.post(url, headers=headers, body=body)

    pprint(request)


def report_link(redditclient):
    url = base_url + '/api/report'

    headers = get_auth_header(redditclient)

    body = redditclient.RedditLinkComment.generate_body()

    request = requests.post(url, headers=headers, body=body)

    pprint(request)


def report_award(redditclient):
    url = base_url + '/api/report_award'

    headers = get_auth_header(redditclient)

    body = redditclient.RedditLinkComment.generate_body()

    request = requests.post(url, headers=headers, body=body)

    pprint(request)


def save_link_or_comment(redditclient):
    url = base_url + '/api/save'

    headers = get_auth_header(redditclient)

    body = redditclient.RedditLinkComment.generate_body()

    request = requests.post(url, headers=headers, body=body)

    pprint(request)


def get_list_saved_categories(redditclient):
    url = base_url + '/api/saved_categories'

    headers = get_auth_header(redditclient)

    body = redditclient.RedditLinkComment.generate_body()

    request = requests.post(url, headers=headers, body=body)

    pprint(request)


def enable_disable_replies_link_or_comment(redditclient):
    url = base_url + '/api/sendreplies'

    headers = get_auth_header(redditclient)

    body = redditclient.RedditLinkComment.generate_body()

    request = requests.post(url, headers=headers, body=body)

    pprint(request)


def set_unset_contestmode_link(redditclient):
    url = base_url + '/api/set_contest_mode'

    headers = get_auth_header(redditclient)

    body = redditclient.RedditLinkComment.generate_body()

    request = requests.post(url, headers=headers, body=body)

    pprint(request)


def set_link_sticky(redditclient):
    url = base_url + '/api/set_subreddit_sticky'

    headers = get_auth_header(redditclient)

    body = redditclient.RedditLinkComment.generate_body()

    request = requests.post(url, headers=headers, body=body)

    pprint(request)


def set_link_suggested_sort(redditclient):
    url = base_url + '/api/set_suggested/sort'

    headers = get_auth_header(redditclient)

    body = redditclient.RedditLinkComment.generate_body()

    request = requests.post(url, headers=headers, body=body)

    pprint(request)


def link_spoiler(redditredditclient):
    url = base_url + '/api/spoiler'

    headers = get_auth_header(redditredditclient)

    body = redditredditclient.RedditLinkComment.generate_body()

    request = requests.post(url, headers=headers, body=body)

    pprint(request)


def link_store_visits(redditclient):
    # requires Reddit Premium

    url = base_url + '/api/store_visits'

    headers = get_auth_header(redditclient)

    body = redditclient.RedditLinkComment.generate_body()

    request = requests.post(url, headers=headers, body=body)

    pprint(request)


def submit_link(redditclient):
    url = base_url + '/api/submit'

    headers = get_auth_header(redditclient)

    body = redditclient.RedditLinkComment.generate_body()

    request = requests.post(url, headers=headers, body=body)

    pprint(request)


def unhide_link(redditclient):
    url = base_url + '/api/unhide'

    headers = get_auth_header(redditclient)

    body = redditclient.RedditLinkComment.generate_body()

    request = requests.post(url, headers=headers, body=body)

    pprint(request)


def unlock_link(redditclient):
    url = base_url + '/api/unlock'

    headers = get_auth_header(redditclient)

    body = redditclient.RedditLinkComment.generate_body()

    request = requests.post(url, headers=headers, body=body)

    pprint(request)


def unmark_link_nsfw(redditclient):
    url = base_url + '/api/unmarknsfw'

    headers = get_auth_header(redditclient)

    body = redditclient.RedditLinkComment.generate_body()

    request = requests.post(url, headers=headers, body=body)

    pprint(request)


def unsave_link_or_comment(redditclient):
    url = base_url + '/api/unsave'

    headers = get_auth_header(redditclient)

    body = redditclient.RedditLinkComment.generate_body()

    request = requests.post(url, headers=headers, body=body)

    pprint(request)


def unspoil_link(redditclient):
    url = base_url + '/api/unspoiler'

    headers = get_auth_header(redditclient)

    body = redditclient.RedditLinkComment.generate_body()

    request = requests.post(url, headers=headers, body=body)

    pprint(request)


def vote_link(redditclient):
    url = base_url + '/api/vote'

    headers = get_auth_header(redditclient)

    body = redditclient.RedditLinkComment.generate_body()

    request = requests.post(url, headers=headers, body=body)

    pprint(request)


##################
## LISTING API
##################


def list_of_trending_subreddits(redditclient):

    url = base_url + '/api/trending_subreddits'

    headers = get_auth_header(redditclient)

    request = requests.get(url,headers=headers)

    pprint(request)


def get_best_listing(redditclient):

    url = base_url + '/best'

    headers = get_auth_header(redditclient)

    body = redditclient.RedditListing.generate_queries()

    request = requests.get(url,headers=headers,params=body)

    pprint(request)

def get_listing_by_id(redditclient):

    url = base_url + '/by_id/names'

    headers = get_auth_header(redditclient)

    body = redditclient.RedditListing.generate_queries()

    request = requests.get(url,headers=headers,params=body)

    pprint(request)

def get_comment_tree_for_given_link(redditclient):

    url = base_url + '[/r/{}]/comments/article'.format(redditclient.RedditListing.get_subreddit_name())

    headers = get_auth_header(redditclient)

    body = redditclient.RedditListing.generate_queries()

    request = requests.get(url,headers=headers,params=body)

    pprint(request)

def list_of_submissions_for_url(redditclient):

    url = base_url + '/duplicates/article'

    headers = get_auth_header(redditclient)

    body = redditclient.RedditListing.generate_queries()

    request = requests.get(url,headers=headers,params=body)

    pprint(request)


def get_hot_list(redditclient):

    url = base_url + '[/r/{}]/hot'.format(redditclient.RedditListing.get_subreddit_name())

    headers = get_auth_header(redditclient)

    body = redditclient.RedditListing.generate_queries()

    request = requests.get(url,headers=headers,params=body)

    pprint(request)

def get_new_listing(redditclient):

    url = base_url + '[/r/{}]/new'.format(redditclient.RedditListing.get_subreddit_name())

    headers = get_auth_header(redditclient)

    body = redditclient.RedditListing.generate_queries()

    request = requests.get(url,headers=headers,params=body)

    pprint(request)


def get_random_listing(redditclient):

    url = base_url + '[/r/{}]/random'.format(redditclient.RedditListing.get_subreddit_name())

    headers = get_auth_header(redditclient)

    body = redditclient.RedditListing.generate_queries()

    request = requests.get(url,headers=headers,params=body)

    pprint(request)

def get_rising_listing(redditclient):

    url = base_url + '[/r/{}]/rising'.format(redditclient.RedditListing.get_subreddit_name())

    headers = get_auth_header(redditclient)

    body = redditclient.RedditListing.generate_queries()

    request = requests.get(url,headers=headers,params=body)

    pprint(request)


def get_sorted_listing(redditclient):

    url = base_url + '[/r/{}]/sort'.format(redditclient.RedditListing.get_subreddit_name())

    headers = get_auth_header(redditclient)

    body = redditclient.RedditListing.generate_queries()

    request = requests.get(url,headers=headers,params=body)

    pprint(request)

def get_top_listing(redditclient):

    url = base_url + '[/r/{}]/top'.format(redditclient.RedditListing.get_subreddit_name())

    headers = get_auth_header(redditclient)

    body = redditclient.RedditListing.generate_queries()

    request = requests.get(url,headers=headers,params=body)

    pprint(request)


def get_controversial_listing(redditclient):

    url = base_url + '[/r/{}]/controversial'.format(redditclient.RedditListing.get_subreddit_name())

    headers = get_auth_header(redditclient)

    body = redditclient.RedditListing.generate_queries()

    request = requests.get(url,headers=headers,params=body)

    pprint(request)


#######################
# LIVE THREADS METHODS
#######################

def get_websocket_url(redditclient):

    url = base_url + '/live/thread/about.json'

    headers = get_auth_header(redditclient)

    request = requests.get(url,headers=headers)

    pprint(request)


def get_listing_live_events(redditclient):

    url = base_url + '/api/live/by_id/names'

    headers = get_auth_header(redditclient)

    body = redditclient.RedditLive.generate_queries()

    request = requests.get(url,headers=headers,params=body,stream=True)

    for data in request.iter_lines():
        print(data)


def create_live_event(redditclient):

    url = base_url + '/api/live/create'

    headers = get_auth_header(redditclient)

    body = redditclient.RedditLive.generate_queries()

    request = requests.post(url,headers=headers,body=body)

    pprint(request)

def live_happening_now(redditclient):

    url = base_url + '/api/live/happening_now'

    headers = get_auth_header(redditclient)

    body = redditclient.RedditLive.generate_queries()

    request = requests.get(url,headers=headers,params=body,stream=True)

    pprint(request)

def accept_contributor_invite(redditclient):

    url = base_url + '/api/live/{}/accept_contributor_invite'.format(redditclient.RedditLive.get_thread_name())

    headers = get_auth_header(redditclient)

    body = redditclient.RedditLive.generate_queries()

    request = requests.post(url,headers=headers,body=body)

    pprint(request)


def close_thread(redditclient):

    url = base_url + '/api/live/{}/close_thread'.format(redditclient.RedditLive.get_thread_name())

    headers = get_auth_header(redditclient)

    body = redditclient.RedditLive.generate_queries()

    request = requests.post(url,headers=headers,body=body)

    pprint(request)


def delete_update(redditclient):

    url = base_url + '/api/live/{}/edit'.format(redditclient.RedditLive.get_thread_name())

    headers = get_auth_header(redditclient)

    body = redditclient.RedditLive.generate_queries()

    request = requests.post(url,headers=headers,body=body)

    pprint(request)


def edit_thread(redditclient):

    url = base_url + '/api/live/{}/edit'.format(redditclient.RedditLive.get_thread_name())

    headers = get_auth_header(redditclient)

    body = redditclient.RedditLive.generate_queries()

    request = requests.post(url,headers=headers,body=body)

    pprint(request)

def hide_discussion(redditclient):

    url = base_url + '/api/live/{}/hide_discussion'.format(redditclient.RedditLive.get_thread_name())

    headers = get_auth_header(redditclient)

    body = redditclient.RedditLive.generate_queries()

    request = requests.post(url,headers=headers,body=body)

    pprint(request)


def invite_contributor(redditclient):

    url = base_url + '/api/live/{}/invite_contributor'.format(redditclient.RedditLive.get_thread_name())

    headers = get_auth_header(redditclient)

    body = redditclient.RedditLive.generate_queries()

    request = requests.post(url,headers=headers,body=body)

    pprint(request)

def leave_contributor(redditclient):

    url = base_url + '/api/live/{}/leave_contributor'.format(redditclient.RedditLive.get_thread_name())

    headers = get_auth_header(redditclient)

    body = redditclient.RedditLive.generate_queries()

    request = requests.post(url,headers=headers,body=body)

    pprint(request)

def report_thread(redditclient):

    url = base_url + '/api/live/{}/report'.format(redditclient.RedditLive.get_thread_name())

    headers = get_auth_header(redditclient)

    body = redditclient.RedditLive.generate_queries()

    request = requests.post(url,headers=headers,body=body)

    pprint(request)

def revoke_contributor_permission(redditclient):

    url = base_url + '/api/live/{}/rm_contributor'.format(redditclient.RedditLive.get_thread_name())

    headers = get_auth_header(redditclient)

    body = redditclient.RedditLive.generate_queries()

    request = requests.post(url,headers=headers,body=body)

    pprint(request)

def revoke_outstanding_contributor_invite(redditclient):

    url = base_url + '/api/live/{}/rm_contributor_invite'.format(redditclient.RedditLive.get_thread_name())

    headers = get_auth_header(redditclient)

    body = redditclient.RedditLive.generate_queries()

    request = requests.post(url,headers=headers,body=body)

    pprint(request)


def set_contributor_permissions(redditclient):

    url = base_url + '/api/live/{}/set_contributor_permissions'.format(redditclient.RedditLive.get_thread_name())

    headers = get_auth_header(redditclient)

    body = redditclient.RedditLive.generate_queries()

    request = requests.post(url,headers=headers,body=body)

    pprint(request)


def strike_listing_update(redditclient):

    url = base_url + '/api/live/{}/strike_update'.format(redditclient.RedditLive.get_thread_name())

    headers = get_auth_header(redditclient)

    body = redditclient.RedditLive.generate_queries()

    request = requests.post(url,headers=headers,body=body)

    pprint(request)

def unhide_comment_or_link(redditclient):

    url = base_url + '/api/live/{}/unhide_discussion'.format(redditclient.RedditLive.get_thread_name())

    headers = get_auth_header(redditclient)

    body = redditclient.RedditLive.generate_queries()

    request = requests.post(url,headers=headers,body=body)

    pprint(request)

def update_thread(redditclient):

    url = base_url + '/api/live/{}/update'.format(redditclient.RedditLive.get_thread_name())

    headers = get_auth_header(redditclient)

    body = redditclient.RedditLive.generate_queries()

    request = requests.post(url,headers=headers,body=body)

    pprint(request)


def get_list_of_updates(redditclient):

    url = base_url + '/live/{}'.format(redditclient.RedditLive.get_thread_name())

    headers = get_auth_header(redditclient)

    body = redditclient.RedditLive.generate_queries()

    request = requests.post(url,headers=headers,body=body)

    pprint(request)


def get_live_thread_info(redditclient):

    url = base_url + '/live/{}/about'.format(redditclient.RedditLive.get_thread_name())

    headers = get_auth_header(redditclient)

    body = redditclient.RedditLive.generate_queries()

    request = requests.post(url,headers=headers,body=body)

    pprint(request)


def get_list_of_contributors(redditclient):

    url = base_url + '/live/{}/contributors'.format(redditclient.RedditLive.get_thread_name())

    headers = get_auth_header(redditclient)

    body = redditclient.RedditLive.generate_queries()

    request = requests.post(url,headers=headers,body=body)

    pprint(request)


def get_list_of_thread_submissions(redditclient):

    url = base_url + '/live/{}/discussions'.format(redditclient.RedditLive.get_thread_name())

    headers = get_auth_header(redditclient)

    body = redditclient.RedditLive.generate_queries()

    request = requests.post(url,headers=headers,body=body)

    pprint(request)


def live_thread_details(redditclient):

    url = base_url + '/live/{}/updates/{}'.format(redditclient.RedditLive.get_thread_name(),redditclient.RedditLive.update_id)

    headers = get_auth_header(redditclient)

    body = redditclient.RedditLive.generate_queries()

    request = requests.post(url,headers=headers,body=body)

    pprint(request)

#######################
# PRIVATE MESSAGES API
#######################

def blocking_author(redditclient):

    url = base_url + '/api/block'

    headers = get_auth_header(redditclient)

    body = redditclient.RedditPrivate.generate_queries()

    request = requests.post(url,headers=headers,body=body)

    pprint(request)


def collapse_message(redditclient):

    url = base_url + '/api/collapse-message'

    headers = get_auth_header(redditclient)

    body = redditclient.RedditPrivate.generate_queries()

    request = requests.post(url,headers=headers,body=body)

    pprint(request)


def compose_message(redditclient):

    url = base_url + '/api/compose'

    headers = get_auth_header(redditclient)

    body = redditclient.RedditPrivate.generate_queries()

    request = requests.post(url,headers=headers,body=body)

    pprint(request)

def delete_message(redditclient):

    url = base_url + '/api/del_msg'

    headers = get_auth_header(redditclient)

    body = redditclient.RedditPrivate.generate_queries()

    request = requests.post(url,headers=headers,body=body)

    pprint(request)


















if __name__ == '__main__':
    client = RedditClient()
    client.add_scope('identity')
    client.add_scope('edit')
    client.add_scope('flair')
    client.add_scope('history')
    client.add_scope('modconfig')
    client.add_scope('modflair')
    client.add_scope('modlog')
    client.add_scope('modposts')
    client.add_scope('modwiki')
    client.add_scope('mysubreddits')
    client.add_scope('privatemessages')
    client.add_scope('read')
    client.add_scope('report')
    client.add_scope('save')
    client.add_scope('submit')
    client.add_scope('subscribe')
    client.add_scope('vote')
    client.add_scope('wikiedit')
    client.add_scope('wikiread')
    implicit_grant_flow(client)
    get_user_identitiy(client)
    get_user_karma(client)
