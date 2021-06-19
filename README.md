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
- [Emoji API](https://www.reddit.com/dev/api#section_emoji)
- [Flair API](https://www.reddit.com/dev/api#section_flair)
- [Reddit Gold API](https://www.reddit.com/dev/api#section_gold)
- [Links & Comments API](https://www.reddit.com/dev/api#section_links_and_comments)
- [Listings API](https://www.reddit.com/dev/api#section_listings)
- [Live Threads API](https://www.reddit.com/dev/api#section_live)
- [Private Messages API](https://www.reddit.com/dev/api#section_messages)
- [Misc API](https://www.reddit.com/dev/api#section_misc)
- [Moderation API](https://www.reddit.com/dev/api#section_moderation)
- [New Modmail API](https://www.reddit.com/dev/api#section_modmail)
- [Multis API](https://www.reddit.com/dev/api#section_multis)
- [Search API](https://www.reddit.com/dev/api#section_search)
- [Subreddits API](https://www.reddit.com/dev/api#section_subreddits)
- [Users API](https://www.reddit.com/dev/api#section_users)
- [Widgets API](https://www.reddit.com/dev/api#section_widgets)
- [Wiki API](https://www.reddit.com/dev/api#section_wiki)
  
  
 
