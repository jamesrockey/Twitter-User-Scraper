class User:
    def __init__(self, scrape_time, id_str, screen_name, name, created_at, protected, location, description, verified,
                 followers_count, friends_count, withheld_in_countries):
        self.scrape_time = scrape_time
        self.id_str = id_str
        self.username = screen_name
        self.name = name
        self.created_at = created_at
        self.protected = protected
        self.location = location
        self.description = description
        self.verified = verified
        self.followers_count = followers_count
        self.friends_count = friends_count
        self.withheld_in_countries = withheld_in_countries
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
        if not location:
            location = 'N/A'
        if not description:
            description = 'N/A'
        if len(banned) == 0:
            banned.append('N/A')
        if self.followers_count == 0:
            recent_followers.append('N/A')
        if self.friends_count == 0:
            recent_friends.append('N/A')
        lst = ["Time last updated: " + str(self.scrape_time), "ID: " + self.id_str, "Username: " + self.username, "Name: " + self.name,
               "Account created at: " + str(self.created_at),
               "Tweets_is_private: " + str(self.protected), "Location: " + location,
               "Description: " + description, "Verified: " + str(self.verified),
               "Followers count: " + str(self.followers_count), "Friend count: " + str(self.friends_count),
               "Content withheld in countries: " + ", ".join(str(elem) for elem in banned),
               "Recent followers: " + ", ".join(str(elem) for elem in recent_followers),
               "Recent friends: " + ", ".join(str(elem) for elem in recent_friends)]

        return "\n".join(lst)
