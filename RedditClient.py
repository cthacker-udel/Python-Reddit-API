class RedditClient:
    
    def __init__(self):
        ## used for token
        self.scopes = []

    def set_username(self,username):
        self.username = username

    def set_password(self,password):
        self.password = password

    def set_client_id(self, client_id):
        self.client_id = client_id

    def set_client_secret(self,secret_key):
        self.client_secret = secret_key

    def set_redirect_uri(self,redirect_uri):
        self.redirect_uri = redirect_uri

    def add_scope(self,the_scope):
        self.scopes.append(the_scope)

    def set_oauth_code(self,the_code):
        self.oauth_code = the_code

    def set_access_token(self,the_token):
        self.access_token = the_token

