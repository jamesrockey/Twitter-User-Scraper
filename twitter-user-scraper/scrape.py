import tweepy
from user import User


def configure_api():
    while True:
        print("Please enter the following information to access Twitter API")
        try:
            # consumer_key = input("Please enter Consumer Key \n").strip()
            # consumer_secret = input("Please enter Consumer Secret Key \n").strip()
            # access_token = input("Please enter Access Token \n").strip()
            # access_token_secret = input("Please enter Access Token Secret \n").strip()

            consumer_key = "Kjc7UDsZHzWfd4deChQC93jYz"
            consumer_secret = "CzQ5yzUSHpMin7cSUPWOGzOiKyLRxPgHg9zPUohHMQ8jBGl7Mz"
            access_token = "1475541055084937219-oDLFr86cjzrj1Uwf2CQQhg3r0slKSa"
            access_token_secret = "xwdxwlx28W9piyrt1QHKtmKDmchRQjdnh06yWBNAF1W5U"

            auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
            auth.set_access_token(access_token, access_token_secret)

            # Construct the api instance
            api = tweepy.API(auth)

            # will throw an exception if invalid, otherwise return api instance
            api.verify_credentials()
        except:
            print("Invalid Credentials, please try again \n")
        else:
            return api


def find_user(api, queried_users):
    username = input("Please enter the username of the user whose data you would like to collect "
                     "(@ symbol not required)\n").strip()
    # remove @ char if included in username input
    if username.find('@') != -1:
        username = username.replace('@', '', 1)
    # if user has already been queried, print username and return
    for user in queried_users:
        if user.username == username:
            print(user.__str__())
            return
    # create and return new user
    new_user = create_user(api, username)
    if (new_user != None):
        print(new_user.__str__())
        return new_user


def create_user(api, username):
    # check if username is exists
    user = None
    try:
        user = api.get_user(screen_name=username)
    except:
        print("Invalid Username please try again")
        return
    else:
        new_user = User(username)
        new_user.name = user.name
        new_user.created_at = user.created_at

        try: # api throws exception for is private variable only
            new_user.tweets_is_private = user.tweets_is_private
        except:
            new_user.tweets_is_private = False
        else:
            new_user.tweets_is_private = True
        new_user.location = user.location
        print("e")
        new_user.description = user.description
        print("f")
        new_user.verified = user.verified
        print("g")
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
        if (c == '1'):
            user = find_user(api, queried_users)
            if user != None:
                queried_users.append(user)
        elif (c == '4'):
            quit()
        print(len(queried_users))
