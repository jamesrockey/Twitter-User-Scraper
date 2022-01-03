class User:
    def __init__(self, username):
        self.username = username
        self.name = None
        self.created_at = None
        self.tweets_is_private = False
        self.location = None
        self.description = None
        self.verified = False

    # returns string information about user to be printed to console
    def __str__(self):
        lst = ["Username: " + self.username, "Name: " + self.name, "Account created at: " + str(self.created_at),
               "Tweets_is_private: " + str(self.tweets_is_private), "Location: " + self.location,
               "Description: " + self.description, "Verified: " + str(self.verified)]
        return ", ".join(lst)
