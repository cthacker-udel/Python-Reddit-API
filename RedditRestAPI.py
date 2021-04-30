import requests
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import DriverManager as FirefoxDriverManager
from webdriver_manager.logger import log
from pprint import pprint
import time

from RedditClient import RedditClient

base_auth_url = 'https://www.reddit.com/api/v1/authorize'

#base_url = 'https://www.reddit.com'

#base_url = 'https://ssl.reddit.com'

base_url = 'https://oauth.reddit.com'

def get_auth_header(client):

    headers = {'Authorization': 'Bearer {}'.format(client.access_token),
               'User-Agent': 'cthacker-udel Reddit API Python Wrapper'}

    return headers


def implicit_grant_flow(client):
    try:
        br = webdriver.Firefox(FirefoxDriverManager().install())
    except Exception as e:
        try:
            br = webdriver.Chrome(ChromeDriverManager().install())
        except Exception as e:
            return None

    queryStringList = []

    params = {'client_id': client.client_id,
              'response_type': 'token',
              'state': 'RANDOM_STRING',
              'redirect_uri': client.redirect_uri,
              'scope': ' '.join(client.scopes)}

    for eachkey in params.keys():
        queryStringList.append('{}={}'.format(eachkey,params[eachkey]))

    queryString = '&'.join(queryStringList)

    url = base_auth_url + '?' + queryString
    print(url)

    br.get(url)

    ### find login box

    log('Filling in username')

    username_box = br.find_element_by_id('loginUsername')
    username_box.send_keys(client.username)

    time.sleep(1)

    log('Filling in password')

    password_box = br.find_element_by_id('loginPassword')
    password_box.send_keys(client.password)

    time.sleep(2)

    login_button = br.find_element_by_xpath('/html/body/div/main/div[1]/div/div[2]/form/fieldset[5]/button').click()

    time.sleep(4)

    log('Allowing Python-Wrapper Reddit API permission')

    allow_button = br.find_element_by_xpath('/html/body/div[3]/div/div[2]/form/div/input[1]').click()

    time.sleep(3)

    log('Acquiring code to generate token')

    curr_url = br.current_url

    response = curr_url.split('&token_type')

    client.set_access_token(response[0].split("access_token=")[1])

    return response


def token_post_request(client):

    url = base_url + '/api/v1/access_token'

    user_agent = {'User-Agent': 'cthacker-udel Reddit API Python Wrapper'}

    client_auth = requests.auth.HTTPBasicAuth(client.client_id,client.client_secret)

    headers = {'User-Agent': 'cthacker-udel Reddit API Python Wrapper'}

    data = {'grant_type': 'authorization_code',
            'code': client.oauth_code,
            'redirect_uri': client.redirect_uri}

    request = requests.post(url,data=data,headers=headers,auth=client_auth)

    pprint(request)



############################################
#       Account Methods
############################################


def get_user_identitiy(client):

    url = base_url + '/api/v1/me'

    headers = get_auth_header(client)

    #client_auth = requests.auth.HTTPBasicAuth(client.client_id, client.client_secret)

    request = requests.get(url,headers=headers).json()

    pprint(request)

    print('\n\n')

    return request


def get_user_identity_features(client):

    identity = get_user_identitiy(client)

    return identity['features']

def get_user_identity_attribute(client,attribute):

    identity = get_user_identitiy(client)

    return identity[attribute]




def get_user_karma(client):

    url = base_url + '/api/v1/me/karma'

    headers = get_auth_header(client)

    request = requests.get(url,headers=headers).json()

    pprint(request)

    return request.status_code == 200


def get_user_preference_settings(client):

    url = base_url + '/api/v1/me/prefs'

    headers = get_auth_header(client)

    request = requests.get(url,headers=headers).json()

    pprint(request)

    return request.status_code == 200


def edit_user_preference_settings(client):

    url = base_url + '/api/v1/me/prefs'

    headers = get_auth_header(client)

    body = client.PreferenceSettings.convert_patch_body()

    request = requests.patch(url,json=body,headers=headers)

    pprint(request)

    return request.status_code == 200


def get_user_trophies(client):

    url = base_url + '/api/v1/me/trophies'

    headers = get_auth_header(client)

    request = requests.get(url,headers=headers)

    pprint(request)

    return request.status_code == 200

def get_preference_settings_where(client):

    url = base_url = '/prefs/{}'.format(client.PreferenceSettings.where)

    headers = get_auth_header(client)

    request = requests.get(url,headers=headers)

    pprint(request)

    return request.status_code == 200

def get_preference_settings_v1(client):

    url = base_url + "/api/v1/me/{}".format(client.PreferenceSettings.where)

    headers = get_auth_header(client)

    request = requests.get(url,headers=headers)

    pprint(request)

    return request.status_code == 200


#################################
# Captcha Methods
#################################


def check_captcha(client):

    url = base_url + "/api/needs_captcha"

    headers = get_auth_header(client)

    request = requests.get(url,headers=headers)

    pprint(request)

    return request.status_code == 200


#################################
# Collections Methods
#################################


def add_post_to_collection(client):

    url = base_url + '/api/v1/collections/add_post_to_collection'

    body = client.RedditCollection.generate_body()

    headers = get_auth_header(client)

    request = requests.post(url,headers=headers,data=body)

    pprint(request)

    return request.status_code == 200


def fetch_collection(client):

    url = base_url + '/api/v1/collections/collection'

    body = client.RedditCollection.generate_body()

    headers = get_auth_header(client)

    request = requests.get(url,headers=headers,body=body)

    pprint(request)

    return request.status_code == 200

def create_collection(client):

    url = base_url + '/api/v1/collections/create_collection'

    body = client.RedditCollection.generate_body()

    headers = get_auth_header(client)

    request = requests.post(url,headers=headers,data=body)

    pprint(request)

    return request.status_code == 200


def delete_collection(client):

    url = base_url + '/api/v1/collections/delete_collection'

    body = client.RedditCollection.generate_body()

    headers = get_auth_header(client)

    request = requests.post(url,headers=headers,data=body)

    pprint(request)

    return request.status_code == 200

def follow_collection(client):

    url = base_url + '/api/v1/collections/follow_collection'

    body = client.RedditCollection.generate_body()

    headers = get_auth_header(client)

    request = requests.post(url,headers=headers,data=body)

    pprint(request)

    return request.status_code == 200

def remove_post_in_collection(client):

    url = base_url + '/api/v1/collections/remove_post_in_collection'

    body = client.RedditCollection.generate_body()

    headers = get_auth_header(client)

    request = requests.post(url,headers=headers,data=body)

    pprint(request)

    return request.status_code == 200


def reorder_collection(client):

    url = base_url + '/api/v1/collections/reorder_collection'

    body = client.RedditCollection.generate_body()

    headers = get_auth_header(client)

    request = requests.post(url,headers=headers,data=body)

    pprint(request)

    return request.status_code == 200


def fetch_subreddit_collections(client):

    url = base_url + '/api/v1/collections/subreddit_collections'

    body = client.RedditCollection.generate_body()

    headers = get_auth_header(client)

    request = requests.get(url,headers=headers,body=body)

    pprint(request)

    return request.status_code == 200

def update_collection_description(client):

    url = base_url + '/api/v1/collections/update_collection_description'

    body = client.RedditCollection.generate_body()

    headers = get_auth_header(client)


    request = requests.post(url,headers=headers,data=body)

    pprint(request)

    return request.status_code == 200

def update_collection_display_layout(client):

    url = base_url + '/api/v1/collections/update_collection_display_layout'

    body = client.RedditCollection.generate_body()

    headers = get_auth_header(client)

    request = requests.post(url,headers=headers,data=body)

    pprint(request)

    return request.status_code == 200

def update_collection_title(client):

    url = base_url + '/api/v1/collections/update_collection_title'

    body = client.RedditCollection.generate_body()

    headers = get_auth_header(client)

    request = requests.post(url,headers=headers,data=body)

    pprint(request)

    return request.status_code == 200



#################################
# EMOJI METHODS
#################################



def add_emoji_to_subreddit(client):

    url = base_url + '/api/v1/{}/emoji.json'.format(client.RedditEmoji.subreddit_name)

    body = client.RedditEmoji.generate_body()

    headers = get_auth_header(client)

    request = requests.post(url,body=body,headers=headers)

    pprint(request)


def delete_subreddit_emoji(client):

    url = base_url + '/api/v1/{}/emoji/{}'.format(client.RedditEmoji.subreddit_name,client.RedditEmoji.name)

    headers = get_auth_header(client)

    request = requests.delete(url,headers=headers)

    pprint(request)


def upload_emoji_asset(client):

    url = base_url + '/api/v1/{}/emoji_asset_upload_s3.json'.format(client.RedditEmoji.subreddit_name)

    headers = get_auth_header(client)

    body = client.RedditEmoji.generate_body()

    request = requests.post(url,headers=headers,data=body)

    pprint(request)


def set_emoji_size(client):

    url = base_url + '/api/v1/{}/emoji_custom_size'.format(client.RedditEmoji.subreddit_name)

    headers = get_auth_header(client)

    body = client.RedditEmoji.generate_body()

    request = requests.post(url,headers=headers,data=body)

    pprint(request)

def get_subreddit_emojis(client):

    url = base_url + '/api/v1/{}/emojis/all'.format(client.RedditEmoji.subreddit_name)

    headers = get_auth_header(client)

    request = requests.get(url,headers=headers)

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
    
    

    

