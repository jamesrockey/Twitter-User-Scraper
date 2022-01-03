class User:
    def __init__(self):
        self.id_str = None
        self.username = None
        self.name = None
        self.created_at = None
        self.protected = False
        self.location = None
        self.description = None
        self.verified = False
        self.followers_count = 0
        self.friends_count = 0
        self.withheld_in_countries = []
        self.recent_followers = []
        self.recent_friends = []

    # returns string information about user to be printed to console
    def __str__(self):
        # check for missing location, description, and withheld countries
        location = self.location
        description = self.description
        banned = self.withheld_in_countries
        recent_followers = self.recent_followers
        recent_friends = self.recent_friends
        if (location == None):
            location = 'N/A'
        if (description == None):
            description = 'N/A'
        if len(banned) == 0:
            banned.append('N/A')
        if self.followers_count == 0:
            recent_followers.append("User has no followers")
        if self.friends_count == 0:
            recent_friends.append("User has no friends")
        lst = ["ID: " + self.id_str, "Username: " + self.username, "Name: " + self.name,
               "Account created at: " + str(self.created_at),
               "Tweets_is_private: " + str(self.protected), "Location: " + location,
               "Description: " + description, "Verified: " + str(self.verified),
               "Followers count: " + str(self.followers_count), "Friend count: " + str(self.friends_count),
               "Content withheld in countries: " + ", ".join(str(elem) for elem in banned),
               "Recent followers: " + ", ".join(str(elem) for elem in recent_followers),
               "Recent friends: " + ", ".join(str(elem) for elem in recent_friends)]

        return "\n".join(lst)
