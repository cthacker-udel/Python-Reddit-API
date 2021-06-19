## Python Reddit API
> Author : Cameron Thacker (University of Delaware)

### Description :

This project is the implementation of Reddit API using Python, combined with the requests module, selenium, and Webdriver Manager.
- The main class of the project is [RedditClient](https://github.com/cthacker-udel/Python-Reddit-API/blob/master/RedditClient.py) which acts as the glue that holds all the other classes together. Each file besides [RedditRestAPI](https://github.com/cthacker-udel/Python-Reddit-API/blob/master/RedditRestAPI.py) imports [RedditClient](https://github.com/cthacker-udel/Python-Reddit-API/blob/master/RedditClient.py), and subclasses to [RedditClient](https://github.com/cthacker-udel/Python-Reddit-API/blob/master/RedditClient.py).
  - [RedditClient](https://github.com/cthacker-udel/Python-Reddit-API/blob/master/RedditClient.py) is subclassed to [RedditRestAPI](https://github.com/cthacker-udel/Python-Reddit-API/blob/master/RedditRestAPI.py), to execute all necessary API method calls, the method calls themself in [RedditRestAPI](https://github.com/cthacker-udel/Python-Reddit-API/blob/master/RedditRestAPI.py) are executed with the assistance of the requests library


#### Implementation:

- [Account API](https://www.reddit.com/dev/api#section_account)
- [Captcha API](https://www.reddit.com/dev/api#section_captcha)
- [Collections API](https://www.reddit.com/dev/api#section_collections)
- Emoji API
- Flair API
- Reddit Gold API
- Links & Comments API
- Listings API
- Live Threads API
- Private Messages API
- Misc API
- Moderation API
- New Modmail API
- Multis API
- Search API
- Subreddits API
- Users API
- Widgets API
- Wiki API
  
  
 
