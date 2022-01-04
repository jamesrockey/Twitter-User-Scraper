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
        self.recent_tweets = []

    # returns string information about user to be printed to console
    def __str__(self):
        # print N/A if any of these fields are empty
        banned = self.withheld_in_countries.copy()
        recent_followers = self.recent_followers.copy()
        recent_friends = self.recent_friends.copy()
        recent_tweets = self.recent_tweets.copy()
        # 3 most retweeted original posts/retweets
        most_retweeted_posts = self.find_N_most_retweeted(3, is_retweet=False)
        most_retweeted_retweets = self.find_N_most_retweeted(3, is_retweet=True)
        favorite_tag = self.find_most_common_tag()
        if not self.location:
            self.location = 'N/A'
        if not self.description:
            self.description = 'N/A'
        if len(banned) == 0:
            banned.append('N/A')
        if self.followers_count == 0:
            recent_followers.append('N/A')
        if self.friends_count == 0:
            recent_friends.append('N/A')
        if len(self.recent_tweets) == 0:
            recent_tweets.append("N/A")
        if len(most_retweeted_posts) == 0:
            most_retweeted_posts.append('N/A')
        if len(most_retweeted_retweets) == 0:
            most_retweeted_retweets.append('N/A')
        if len(favorite_tag) == 0:
            self.favorite_tag = 'N/A'
        lst = ["Time last updated: " + str(self.scrape_time), "ID: " + self.id_str, "Username: " + self.username, "Name: " + self.name,
               "Account created at: " + str(self.created_at),
               "Tweets_is_private: " + str(self.protected), "Location: " + self.location,
               "Description: " + self.description, "Verified: " + str(self.verified),
               "Followers count: " + str(self.followers_count), "Friend count: " + str(self.friends_count),
               "Content withheld in countries: " + ", ".join(str(elem) for elem in banned),
               "Recent followers: " + ", ".join(str(elem) for elem in recent_followers),
               "Recent friends: " + ", ".join(str(elem) for elem in recent_friends),
               "Favorite Hashtag: " + favorite_tag,
               "Most retweeted posts: \n\n" + "\n \n".join(tweet.__str__() for tweet in most_retweeted_posts),
               "\nMost retweeted retweets: \n\n" + "\n \n".join(tweet.__str__() for tweet in most_retweeted_retweets)]


        return "\n".join(lst)

    def find_N_most_retweeted(self, N, is_retweet):
        # finds N posts with most retweets, original posts and retweeted
        tweets = self.recent_tweets.copy()
        max_tweets = []
        if len(tweets) < N:
            N = len(tweets)
        for i in range(0, N):
            max = 0
            max_tweet = None
            for j, tweet in enumerate(tweets):
                if tweet.is_retweet == is_retweet and tweet.retweet_count > max:
                    max = tweet.retweet_count
                    max_tweet = tweet
            if max_tweet:
                max_tweets.append(max_tweet)
                tweets.remove(max_tweet)
        return max_tweets


    def find_all_hashtags(self):
        if not self.protected:
            tags_to_occurrence = {}
            # find all hashtags
            for tweet in self.recent_tweets:
                for word in tweet.text.split():
                    if word.startswith("#"):
                        if word in tags_to_occurrence:
                            tags_to_occurrence[word] += 1
                        else:
                            tags_to_occurrence[word] = 1
        return tags_to_occurrence

    def find_most_common_tag(self):
        tags_to_occurrence = self.find_all_hashtags()
        max_occurrence = 0
        favorite_tag = ''
        for key in tags_to_occurrence.keys():
            if tags_to_occurrence[key] > max_occurrence:
                max_occurrence = tags_to_occurrence[key]
                favorite_tag = key
        return favorite_tag