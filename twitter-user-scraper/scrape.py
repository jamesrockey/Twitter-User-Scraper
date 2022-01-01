import tweepy


def get_valid_api():
    while True:
        try:
            consumer_key = input("Please enter Consumer Key \n").strip()
            consumer_secret = input("Please enter Consumer Secret Key \n").strip()
            access_token = input("Please enter Access Token \n").strip()
            access_token_secret = input("Please enter Access Token Secret \n").strip()

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


if __name__ == "__main__":
    # get valid tweepy api instance
    api = get_valid_api()
