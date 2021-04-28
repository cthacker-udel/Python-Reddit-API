import requests
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import DriverManager as FirefoxDriverManager
from webdriver_manager.manager import DriverManager
from webdriver_manager.logger import log
import uuid
from pprint import pprint
from splinter import Browser
import time
import base64

from RedditClient import RedditClient

base_auth_url = 'https://www.reddit.com/api/v1/authorize'

base_url = 'https://www.reddit.com'


def oauth_code(client):
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

    time.sleep(1)

    login_button = br.find_element_by_xpath('/html/body/div/main/div[1]/div/div[2]/form/fieldset[5]/button').click()

    time.sleep(3)

    log('Allowing Python-Wrapper Reddit API permission')

    allow_button = br.find_element_by_xpath('/html/body/div[3]/div/div[2]/form/div/input[1]').click()

    time.sleep(2)

    log('Acquiring code to generate token')

    curr_url = br.current_url

    response = curr_url.split('=')

    client.set_access_token(response[1])

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















if __name__ == '__main__':

    client = RedditClient()
    client.set_redirect_uri('exampleredirect')
    client.set_client_id('exampleclientid')
    client.set_client_secret('exampleclientsecret')
    client.set_username('exampleusername')
    client.set_password('examplepassword')
    client.add_scope('identity')
    client.add_scope('edit')
    oauth_code(client)
    
    

    

