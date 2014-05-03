import couchdb
import sys
from textblob import TextBlob
import random
import codecs
UTF8Writer = codecs.getwriter('utf8')
sys.stdout = UTF8Writer(sys.stdout)

server = couchdb.Server('http://115.146.93.184:5984')

try:
    db = server['philadelphia']
except:
    print "DB not found. Closing"
    sys.exit(2)

from couchdb.design import ViewDefinition


# results = db.query()
#
# print len(results)

rand = random.sample(range(900000), 40)
j = 0
for i in range(40):
    num = rand[i]
    for r in db.view('test/test', limit=10, startkey=num):
        print j, r.value
        j+=1