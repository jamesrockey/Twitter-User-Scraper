import tweepy
import time
import jsonpickle
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
            # update user's N most retweeted posts/retweets
            new_user.update_N_most_retweeted(3, is_retweet=False)
            new_user.update_N_most_retweeted(3, is_retweet=True)
            new_user.find_most_common_tag()
        return new_user



def save_to_JSON(queried_users):
    path = 'user_data.json'
    jsonpickle.set_encoder_options('json', sort_keys=True, indent=4)
    json_str = jsonpickle.encode(queried_users)
    with open(path, 'w') as outfile:
        outfile.write(json_str)
    outfile.close()

def load_from_JSON():
    path = 'user_data.json'
    queried_users = []
    with open(path, 'r') as infile:
        try:
            data = infile.read()
            queried_users = jsonpickle.decode(data)
        except:
            print("Failed to load users, please clear the file and start searches again")
    infile.close()
    return queried_users

def clear_JSON_file():
    path = 'user_data.json'
    with open(path, 'w') as outfile:
        outfile.truncate()
    outfile.close()

def update_queries(api, queried_users):
    updated_users = []
    for user in queried_users:
        new_user = create_user(api, user.username)
        updated_users.append(new_user)
    return updated_users



if __name__ == "__main__":
    # get valid tweepy api instance
    api = configure_api()

    # begin command line application
    questions = ['Find User', 'Save to .JSON', 'Import from JSON', 'Clear saved queries JSON file', 'Terminate Program']

    # list of queried users from current
    queried_users = []
    while True:
        print('Please enter number corresponding to your choice in the command line')
        for i, option in enumerate(questions, start=1):
            print('(', i, ') ', option)

        c = input().strip()
        if c == '1':
            # print usernames of already queried users
            print("Queried users: " + ", ".join(user.username for user in queried_users))
            username = input("Please enter the username of the user whose data you would like to collect "
                             "(@ char not required)\n").strip()
            user = find_user(username, queried_users)
            if user is None: # if user has not been queried, create new user
                user = create_user(api, username)
                if user is None: # if improper username credentials, continue application
                    continue
                queried_users.append(user)
            print(user.__str__())
        elif c == '2':
            save_to_JSON(queried_users)
        elif c == '3':
            queried_users = load_from_JSON()
        elif c == '4':
            clear_JSON_file()
        elif c == '5':
            queried_users = update_queries(api, queried_users)
        elif c == '6':
            quit()
