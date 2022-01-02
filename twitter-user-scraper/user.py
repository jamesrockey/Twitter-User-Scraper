class User:
    def __init__(self, username):
        self.username = username
        self.name = None
        self.created_at = None
        self.tweets_is_private = False
        self.location = None
        self.description = None
        self.verified = False
