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
ckey = "bE8mJjTd9OMxa2TPsYddItM2u"
csecret = "wUetoc7ofwnoNUSph2GGE3OolHnedLSDTCDTlLmV1a2Y0y1r5W"
atoken = "115946548-i3fTl9Bret21MhN4alKSBZdmVz3GW4sbkDSfzPZ0"
asecret = "0Y6cWPeaESBGU6Saak7ps3bq682Kb8GJaSx1Tn4wCHFLR"
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
    db = server.database('philadelphiaeast')
    
'''===============LOCATIONS=============='''    
twitterStream.filter(locations=[-75.14,39.849083,-74.955076,40.137992]) #PHILLY EAST
# twitterStream.filter(track = ["airport", "car"])
#twitterStream.filter(locations=[-75.330428,39.849083,-75.14,40.137992]) #PHILLY WEST
#twitterStream.filter(locations=[-75.14,39.849083,-74.955076,40.137992]) #PHILLY EAST
#twitterStream.filter(locations=[-75.330428,39.849083,-74.955076,40.137992]) #PHILLY ALL

#twitterStream.filter(locations=[144.829543,-37.966766,144.962775,-37.659376])  #MELBOURNE WEST
#twitterStream.filter(locations=[144.962775,-37.966766,145.096007,-37.659376])  #MELBOURNE EAST
#twitterStream.filter(locations=[144.829543,-37.966766,145.096007,-37.659376])  #MELBOURNE