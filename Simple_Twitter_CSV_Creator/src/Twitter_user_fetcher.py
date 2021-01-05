import tweepy
import pandas as pd

#personal credentials can not be provided, due to submiting publically on github
#enter your personal credentials for code to run (signing up as a twitter developer)
consumer_key = "enter consumer code"
consumer_secret = "enter consumer secret code"
access_token = "enter access token code"
access_token_secret = "enter access token secret code"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)

#creating a list of tweets
tweets = []

#username of twitter user to fetch tweets from
username = 'PlayStation'
#number of tweets to fetch
tweets_num = 50

# a method used to take a given users tweets and converts them to a file (.txt or .csv)
# 
def tweets_to_file(username,tweets_num, filename):
        #loop through each tweet of a given user
        for tweet in api.user_timeline(id=username, count=tweets_num):

            #appending a tweet to a list of all tweets
            tweets.append((tweet.created_at,tweet.id,tweet.text))

            #data frame of needed column data
            df = pd.DataFrame(tweets,columns=['Date', 'Tweet_ID', 'Message'])

            #convert to txt file
            #can alter the file type to .txt or .csv
            #in this example it will simply convert data frame to text file
            df.to_csv(filename)


#calling the function to create the CSV file
print('simple python program to use test the twitter API')
tweets_to_file(username, tweets_num, 'fetched_tweets1.txt')
print('done, tweets have been written onto fetched_tweets1.txt')