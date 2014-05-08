'''
Created on Apr 18, 2014

MELBOURNE EAST
==============
'''
import couchdb
import sys
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


if len(sys.argv)!=3:
    sys.stderr.write("Error: needs more arguments: <URL><DB name>\n")
    sys.exit()

URL = sys.argv[1]
db_name = sys.argv[2]


'''========couchdb'=========='''
server = couchdb.Server(URL)  #('http://115.146.93.184:5984/')
try:
    db = server[db_name]
except:
    sys.stderr.write("Error: DB not found. Closing...\n")
    sys.exit()


'''===============LOCATIONS=============='''

# twitterStream.filter(locations=[144.962775,-37.966766,145.096007,-37.659376])  #MELBOURNE EAST
#
# twitterStream.filter(locations=[144.1995,-37.8086,144.9875,-37.2546])   #NO
# twitterStream.filter(locations=[144.9411,-37.8129,145.6988,-37.2546])   #NE
# twitterStream.filter(locations=[144.422,-38.1182,144.982,-37.8057])     #SO
# twitterStream.filter(locations=[144.9466,-38.1182,145.6027,-37.8057])   #SE


# twitterStream.filter(locations=[-75.410766,39.993373,-75.105452,40.257572]) #NO
# twitterStream.filter(locations=[-75.159453,39.972328,-74.71269,40.257572])
twitterStream.filter(locations=[-75.543975,39.727729,-75.117811,40.024511])
# twitterStream.filter(locations=[-75.159453,39.972328,-74.71269,40.257572])




# twitterStream.filter(track = ["airport", "car"])
#twitterStream.filter(locations=[-75.117733,39.867004,-75.036748,40.137992]) #PHILLY WEST
#twitterStream.filter(locations=[-75.036748,39.867004,-74.955763,40.137992]) #PHILLY EAST
#twitterStream.filter(locations=[-75.117733,39.867004,-74.955763,40.137992]) #PHILLY ALL

#twitterStream.filter(locations=[144.829543,-37.966766,144.962775,-37.659376])  #MELBOURNE WEST
#twitterStream.filter(locations=[144.962775,-37.966766,145.096007,-37.659376])  #MELBOURNE EAST
#twitterStream.filter(locations=[144.829543,-37.966766,145.096007,-37.659376])  #MELBOURNE