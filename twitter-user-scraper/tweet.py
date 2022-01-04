class Tweet:
    def __init__(self, id, text, user, author, favorite_count, retweet_count):
        self.id = id
        self.text = text
        self.user = user
        self.author = author
        self.favorite_count = favorite_count
        self.retweet_count = retweet_count
        self.url = "https://twitter.com/twitter/statuses/" + id
        self.is_retweet: bool
        # check text to see if post is retweet

        if text.find('RT @') == 0:
            self.is_retweet = True
        else:
            self.is_retweet = False

    def __str__(self):
        lst = ["ID: " + self.id, "Text: " + self.text, "Author: " + self.user, "Favorite count: " +
               str(self.favorite_count), "Retweet count: " + str(self.retweet_count),
               "Url: " + self.url, "Is Retweet: " + str(self.is_retweet)]
        return "\n".join(lst)