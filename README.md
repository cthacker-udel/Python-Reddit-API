## Python Reddit API
> Author : Cameron Thacker (University of Delaware)

### Description :

This project is the implementation of Reddit API using Python, combined with the requests module, selenium, and Webdriver Manager.
- The main class of the project is RedditClient which acts as the glue that holds all the other classes together. Each file besides RedditRestAPI imports RedditClient, and subclasses to RedditClient.
  - RedditClient is subclassed to RedditRestAPI, to execute all necessary API method calls, the method calls themself in RedditRestAPI are executed with the assistance of the requests library
  
  
 
