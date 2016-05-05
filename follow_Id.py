import tweepy
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
import time
import os
import datetime
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
pass_criteria = ["software", "java", "developer", "engineer", "Intellij"]
current_count = 0
origin_file_name = "/home/ec2-user/twitter/ids_to_follow/ids_0.txt"
swap_file_name = "/home/ec2-user/twitter/ids_to_follow/ids_0.txt.swap"
unfollow_file_name = "/home/ec2-user/twitter/ids_to_unfollow/ids_0.txt"
with open(unfollow_file_name, "a") as unfollow_file:
    with open(swap_file_name, "w+") as swap_file:
        with open(origin_file_name, "r") as origin_file:
            print datetime.datetime.utcnow()
            for line in origin_file:
                if current_count < 8:
                    try:
                        user = api.get_user(line)
                        user_info = str(user).lower()
                        match = False 
                        for word in pass_criteria:
                            if word in user_info:
                                match = True
                        if match: 
                            print "Following " + line 
                            api.create_friendship(line)
                            unfollow_file.write(line)
                            current_count= current_count + 1
                        else :
                            print "Ignore " + line                    
                    except Exception:
                        print "Exception caught, ignore "  + line     
                    time.sleep(10)       
                else:
                    #print "Skipping " + line
                    swap_file.write(line) 
     
os.rename(swap_file_name, origin_file_name)
       
     
#i#tweepy.API.create_friendship("1084924951")
#for follower in  tweepy.Cursor(api.followers, id = 'intellijidea').items(5):
#    follower.follow()
#    print follower.screen_name

#621961831
#api.create_friendship('621961831')
