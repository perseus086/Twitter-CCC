'''
Created on Apr 18, 2014

PHILADELPHIA EAST
'''
import couchdb
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json

#############API JUAN######
ckey = "B1HlExt5hX2dRIcLGAii1cuhx"
csecret = "QKXeMBO5uS1g2nSYYZpbbTpX8UCTucnHXWPT3gRB8LoJ7oRRXS"
atoken = "115946548-mI65N9dqxbpg6DI3Vw2TVxct7voX5nUMzVEHiR5S"
asecret = "o8pi9ysfPTZD0V0dkrE6F4U4rQqghsWOsDXRq8qNNOeLC"
##################

class listener(StreamListener):
    
    def on_data(self, data):
        dictTweet = json.loads(data)
        try:
            dictTweet["_id"] = str(dictTweet['id'])
            doc = db.save(dictTweet)
            print "SAVED" + str(doc) +"=>" + str(data)
        except:
            print "Already exists"
            pass
        return True
    
    def on_error(self, status):
        print status
        
auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
twitterStream = Stream(auth, listener())

'''========couchdb'=========='''
server = couchdb.Server('http://localhost:5984/')
try:
    db = server.create('philadelphiaeast')
except:
    db = server['philadelphiaeast']
    
'''===============LOCATIONS=============='''    
twitterStream.filter(locations=[-75.14,39.849083,-74.955076,40.137992]) #PHILLY EAST
# twitterStream.filter(track = ["airport", "car"])
#twitterStream.filter(locations=[-75.330428,39.849083,-75.14,40.137992]) #PHILLY WEST
#twitterStream.filter(locations=[-75.14,39.849083,-74.955076,40.137992]) #PHILLY EAST
#twitterStream.filter(locations=[-75.330428,39.849083,-74.955076,40.137992]) #PHILLY ALL

#twitterStream.filter(locations=[144.829543,-37.966766,144.962775,-37.659376])  #MELBOURNE WEST
#twitterStream.filter(locations=[144.962775,-37.966766,145.096007,-37.659376])  #MELBOURNE EAST
#twitterStream.filter(locations=[144.829543,-37.966766,145.096007,-37.659376])  #MELBOURNE