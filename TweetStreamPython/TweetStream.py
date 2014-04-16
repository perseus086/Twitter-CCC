'''
Tweeter stream by location


'''
import couchdb
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json

ckey = "6Zyv4XxVypDqHDpFoHwSTrMzX"
csecret = "3J5TpltHtmEZGEw8RhRLABc3KQ2Quhjj2SVVykfw5zs02fjtpC"
atoken = "153168970-C8H0rPCjztDmLQMrjtgOYSPIzjLMyegrtrAZQQrq"
asecret = "WxWpMOMlghN1tVYZRFugRWTefM1SShLWVI4lL4oPWTAlO"

class listener(StreamListener):
    
    def on_data(self, data):
        
        db.save(json.loads(data))
        print data
        return True
    
    def on_error(self, status):
        print status
        
auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
twitterStream = Stream(auth, listener())

'''couchdb'''
server = couchdb.Server()
try:
    db = server.create('philly-test')
except:
    db = server['philly-test']


# twitterStream.filter(track = ["airport", "car"])
twitterStream.filter(locations=[-75.280303,39.867004,-74.955763,40.137992]) #PHILLY
#twitterStream.filter(locations=[144.3945,-38.2607,145.7647,-37.4598])  #MELBOURNE
