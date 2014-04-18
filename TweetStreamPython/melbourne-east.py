'''
Created on Apr 18, 2014

MELBOURNE EAST
==============
'''
import couchdb
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json


###API PAUL########################
ckey = "6Zyv4XxVypDqHDpFoHwSTrMzX"
csecret = "3J5TpltHtmEZGEw8RhRLABc3KQ2Quhjj2SVVykfw5zs02fjtpC"
atoken = "153168970-C8H0rPCjztDmLQMrjtgOYSPIzjLMyegrtrAZQQrq"
asecret = "WxWpMOMlghN1tVYZRFugRWTefM1SShLWVI4lL4oPWTAlO"
#####################################

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
server = couchdb.Server('http://localhost:5984/')  #('http://115.146.93.184:5984/')
try:
    db = server.create('melbourneeast')
except:
    db = server.database('melbourneeast')
    
'''===============LOCATIONS=============='''    

twitterStream.filter(locations=[144.962775,-37.966766,145.096007,-37.659376])  #MELBOURNE EAST

# twitterStream.filter(track = ["airport", "car"])
#twitterStream.filter(locations=[-75.117733,39.867004,-75.036748,40.137992]) #PHILLY WEST
#twitterStream.filter(locations=[-75.036748,39.867004,-74.955763,40.137992]) #PHILLY EAST
#twitterStream.filter(locations=[-75.117733,39.867004,-74.955763,40.137992]) #PHILLY ALL

#twitterStream.filter(locations=[144.829543,-37.966766,144.962775,-37.659376])  #MELBOURNE WEST
#twitterStream.filter(locations=[144.962775,-37.966766,145.096007,-37.659376])  #MELBOURNE EAST
#twitterStream.filter(locations=[144.829543,-37.966766,145.096007,-37.659376])  #MELBOURNE