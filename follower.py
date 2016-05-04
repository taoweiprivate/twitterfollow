import tweepy
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
import time

#Use your keys
consumer_key = 's0eixJNrfdP1uYXaOU7tw3LKh'
consumer_secret = '937aR1NFJ10WA3IKTQi4SNxq1yxGWzCOpX5CXiqEw6vOz3td1u'
access_token = '727204642875146240-2AEIQyXfsoxRhFAdLInaaA2u0uB0V4V'
access_secret = 'ZHL5ssF8pclyZd9MrtDlQIRU6toT4QnxB03ecTwlQG0YB'


auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

#class TweetListener(StreamListener):
#    def on_status(self, status):
#      print "tweet " + str(status.created_at) +"\n"
#      print status.text + "\n"
#      # You can dump your tweets into Json File, or load it to your database

#stream = Stream(auth, TweetListener(), secure=True, )
#t = u"#python" # You can use different hashtags
#stream.filter(track=[
current_batch = 0
for ids in tweepy.Cursor(api.followers_ids, id = 'intellijidea').pages():
    file_name = "ids_" + str(current_batch) + ".txt"
    with open(file_name, "a") as myfile:
       for current_id in ids:
           myfile.write(str(current_id)+"\n")
           print current_id
    time.sleep(60)
    current_batch = current_batch + 1
       
     
#i#tweepy.API.create_friendship("1084924951")
#for follower in  tweepy.Cursor(api.followers, id = 'intellijidea').items(5):
#    follower.follow()
#    print follower.screen_name

#621961831
#api.create_friendship('621961831')
