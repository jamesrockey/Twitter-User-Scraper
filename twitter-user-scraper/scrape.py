import tweepy
import time
import webbrowser
from user import User
from tweet import Tweet


def configure_api():
    while True:
        try:
            consumer_key = "Kjc7UDsZHzWfd4deChQC93jYz"
            consumer_secret = "CzQ5yzUSHpMin7cSUPWOGzOiKyLRxPgHg9zPUohHMQ8jBGl7Mz"
            callback_uri = 'oob'
            auth = tweepy.OAuthHandler(consumer_key, consumer_secret, callback_uri)
            redirect_url = auth.get_authorization_url()
            webbrowser.open(redirect_url)
            user_pin_input = input("Please enter pin from Twitter verification\n").strip()
            auth.get_access_token(user_pin_input)

            # Construct the api instance
            api = tweepy.API(auth, wait_on_rate_limit=True)

            # will throw an exception if invalid, otherwise return api instance
            api.verify_credentials()
        except:
            print("Invalid Credentials, please try again \n")
        else:
            return api


def find_user(username, queried_users):
    # remove @ char if included in username input
    if username.find('@') != -1:
        username = username.replace('@', '', 1)
    # if user has already been queried, print user info and return
    for user in queried_users:
        if user.username == username:
            return user
    return None


def create_user(api, username):
    # check if username is exists
    user = None
    try:
        user = api.get_user(screen_name=username, tweet_mode='extended')
    except:
        print("Invalid Username please try again")
    else:
        # instantiate new user info

        new_user = User(time.asctime(), user.id_str, user.screen_name, user.name, user.created_at, user.protected,
                        user.location, user.description, user.verified, user.followers_count, user.friends_count,
                        user.withheld_in_countries)
        # If the user is not protected, gather list of user's recent followers, friends, and tweets
        if not new_user.protected:
            for friend in user.friends():
                new_user.recent_friends.append(friend.screen_name)
            for follower in user.followers():
                new_user.recent_followers.append(follower.screen_name)

            timeline = user.timeline()
            for i, status in enumerate(timeline):
                tweet = Tweet(status.id_str, status.text, status.user.screen_name, status.author.screen_name,
                              status.favorite_count, status.retweet_count)
                new_user.recent_tweets.append(tweet)
            new_user.most_retweeted_posts = new_user.update_N_most_retweeted(3, is_retweet=False)
            new_user.most_retweeted_retweets = new_user.update_N_most_retweeted(3, is_retweet=True)
        return new_user





if __name__ == "__main__":
    # get valid tweepy api instance
    api = configure_api()

    # begin command line application
    questions = ['Find User', 'Save to CSV File', 'Import from CSV', 'Terminate Program']

    # list of queried users from current
    queried_users = []
    while True:
        print('Please enter number corresponding to your choice in the command line')
        for i, option in enumerate(questions, start=1):
            print('(', i, ') ', option)

        c = input().strip()
        if c == '1':
            username = input("Please enter the username of the user whose data you would like to collect "
                             "(@ char not required)\n").strip()
            user = find_user(username, queried_users)
            if user is None: # if user has not been queried, create new user
                user = create_user(api, username)
                if user is None: # if improper username credentials, continue application
                    continue
                queried_users.append(user)
            print(user.__str__())
        elif (c == '4'):
            quit()
        print(len(queried_users))
