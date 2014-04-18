'''
Created on Apr 18, 2014

Melbourne WEST
==============
'''
import couchdb
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json

##########API JOSE ############

ckey = "BFzpasIVWffK9EqeVCpWA"
csecret = "rFCm2rr0Dco8HXL6AByK4K5H1b2cKsJcV281QyyrM"
atoken = "45959179-cHy943sIATRHbPdOiAo79GtGH4BjknZxyWSWMGT8N"
asecret = "unQYxMs8jY4hFcYgTXFjeuXDcEyefBk0L14H7I2otw99M"
################################

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
    db = server.create('melbournewest')
except:
    db = server.database('melbournewest')
    
'''===============LOCATIONS=============='''    
twitterStream.filter(locations=[144.829543,-37.966766,144.962775,-37.659376])  #MELBOURNE WEST

# twitterStream.filter(track = ["airport", "car"])
#twitterStream.filter(locations=[-75.117733,39.867004,-75.036748,40.137992]) #PHILLY WEST
#twitterStream.filter(locations=[-75.036748,39.867004,-74.955763,40.137992]) #PHILLY EAST
#twitterStream.filter(locations=[-75.117733,39.867004,-74.955763,40.137992]) #PHILLY ALL

#twitterStream.filter(locations=[144.829543,-37.966766,144.962775,-37.659376])  #MELBOURNE WEST
#twitterStream.filter(locations=[144.962775,-37.966766,145.096007,-37.659376])  #MELBOURNE EAST
#twitterStream.filter(locations=[144.829543,-37.966766,145.096007,-37.659376])  #MELBOURNE