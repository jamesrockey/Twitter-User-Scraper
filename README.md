# Twitter User Scraper
Twitter User Scraper is a command line application that utilizes Twitter's API through the tweepy package using as little api calls as possible. This application also uses the jsonpickle package to save and load user data to a json file.

Installation
------------
To install the required packages, run the following command in your terminal:

    make init
    
To run the program, run the following command in your terminal:
    
    make run
    
You will then be prompted to allow the application to access your twitter account. Once you allow permission, you will be able to scrape user data.

Using the application
---------------------
After configuring the api, you will be prompted to respond to one of the many prompts. Choosing the following numbers has these effects.

1) Choosing 1 does the following: If a user has already been queried user information will be printed to the consol. If the user has not been queried, application will gather user information and then print to the consol.
2) Choosing 2 saves queried users to a json file (user_data.json), which can then be reloaded at another time of use.
3) Choosing 3 reloads previously queried users from user_data.json, which will then be accessable via the command line.
4) Choosing 4 deletes the contents of user_data.json
5) Choosing 5 updates the current list of user-queries with most recent information
6) Choosing 6 terminates the program.

Information Gathered:
--------------------
In it's current implementation, this scraper tool maximizes the number of unique user api searches as possible. Each api call gathers the information about each user:
- The time the most recent scrape was performed
- User's id string
- User's username
- User's name
- If user's account is private or public
- User's location
- User's description
- If the user is verified
- User's follower count
- User's friend (following) count 
- If the user's posts are witheld in any country
- User's 20 most recent followers
- User's 20 most recent friends (following)
- User's 20 most recent tweets

From this information, other useful information such as N most rewteeted original posts, N most retweeted tweets, and favorite hashtag are created.

## **Resources**
- Feel free to reach me at jmsneilrock@gmail.com with any questions or suggestions!


