import json
import random
import codecs
import sys

UTF8Writer = codecs.getwriter('utf8')
sys.stdout = UTF8Writer(sys.stdout)

name = sys.argv[1]

f = open(name,'r')
data = json.load(f)

r = random.sample(range(1000),500)
j = 0
for i in range(len(data["rows"])):
    if i in r:
        print str(j) + ','+ repr(data["rows"][i]["value"])
        j+=1
f.close()