import tweepy


def configure_api():
    while True:
        print("Please enter the following information to access Twitter API")
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
    api = configure_api()
    api.lookup_users('elon_musk')
    # begin command line application

    questions = ['Find User', 'Save to CSV File', 'Import from CSV', 'Terminate Program']
    while True:
        print('Please enter number corresponding to your choice in the command line')
        for i, option in enumerate(questions, start=1):
            print('(', i, ') ', option)
        c = input().strip()
        if (c == '1'):
            continue
        elif (c == '4'):
            break



