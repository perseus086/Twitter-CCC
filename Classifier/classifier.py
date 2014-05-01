'''
CLASSIFIER


'''
from idlelib.IOBinding import encoding
import re
import couchdb
import sys
import json
from textblob import TextBlob


def dictionaries():

    dict_of_sentiments = {}
    dict_of_sentiments[56833]=u'happy'
    dict_of_sentiments[56834]=u'happy'
    dict_of_sentiments[56835]=u'happy'
    dict_of_sentiments[56836]=u'happy'
    dict_of_sentiments[56837]=u'happy'
    dict_of_sentiments[56838]=u'happy'
    dict_of_sentiments[56841]=u'happy'
    dict_of_sentiments[56842]=u'happy'
    dict_of_sentiments[56843]=u'happy'
    dict_of_sentiments[56844]=u'happy'
    dict_of_sentiments[56845]=u'love'
    dict_of_sentiments[56847]=u'happy'
    dict_of_sentiments[56856]=u'kiss'
    dict_of_sentiments[56860]=u'happy'
    dict_of_sentiments[56861]=u'happy'
    dict_of_sentiments[56882]=u'happy'
    dict_of_sentiments[56883]=u'happy'
    dict_of_sentiments[56888]=u'happy'
    dict_of_sentiments[56889]=u'happy'
    dict_of_sentiments[56890]=u'happy'
    dict_of_sentiments[56891]=u'love'
    dict_of_sentiments[56892]=u'happy'
    dict_of_sentiments[56893]=u'kiss'
    dict_of_sentiments[56850]=u'unamused'
    dict_of_sentiments[56851]=u'sad'
    dict_of_sentiments[56852]=u'sad'
    dict_of_sentiments[56854]=u'confounded'
    dict_of_sentiments[56862]=u'sad'
    dict_of_sentiments[56868]=u'angry'
    dict_of_sentiments[56869]=u'sad'
    dict_of_sentiments[56872]=u'sad'
    dict_of_sentiments[56873]=u'sad'
    dict_of_sentiments[56874]=u'relieved'
    dict_of_sentiments[56875]=u'sad'
    dict_of_sentiments[56877]=u'cry'
    dict_of_sentiments[56880]=u'sad'
    dict_of_sentiments[56881]=u'bored'
    dict_of_sentiments[56885]=u'sad'
    dict_of_sentiments[56894]=u'sad'
    dict_of_sentiments[56895]=u'sad'
    dict_of_sentiments[56896]=u'weary'
    dict_of_sentiments[56901]=u'no'
    dict_of_sentiments[56903]=u'sad'
    dict_of_sentiments[56864]=u'angry'
    dict_of_sentiments[56865]=u'furious'
    dict_of_sentiments[56911]=u'beg'
    dict_of_sentiments[56903]=u'tired'


    # happy_dict = []
    # happy_dict.append(u'\U0001F601')
    # happy_dict.append(u'\U0001F602')
    # happy_dict.append(u'\U0001F603')
    # happy_dict.append(u'\U0001F604')
    # happy_dict.append(u'\U0001F605')
    # happy_dict.append(u'\U0001F606')
    # happy_dict.append(u'\U0001F609')
    # happy_dict.append(u'\U0001F60A')
    # happy_dict.append(u'\U0001F60B')
    # happy_dict.append(u'\U0001F60C')
    # happy_dict.append(u'\U0001F60D')
    # happy_dict.append(u'\U0001F60F')
    # happy_dict.append(u'\U0001F618')
    # happy_dict.append(u'\U0001F61C')
    # happy_dict.append(u'\U0001F61D')
    # happy_dict.append(u'\U0001F632')
    # happy_dict.append(u'\U0001F633')
    # happy_dict.append(u'\U0001F638')
    # happy_dict.append(u'\U0001F639')
    # happy_dict.append(u'\U0001F63A')
    # happy_dict.append(u'\U0001F63B')
    # happy_dict.append(u'\U0001F63C')
    # happy_dict.append(u'\U0001F63D')
    #
    # sad_dict = []
    # sad_dict.append(u'\U0001F612')
    # sad_dict.append(u'\U0001F613')
    # sad_dict.append(u'\U0001F614')
    # sad_dict.append(u'\U0001F616')
    # sad_dict.append(u'\U0001F61E')
    # sad_dict.append(u'\U0001F625')
    # sad_dict.append(u'\U0001F628')
    # sad_dict.append(u'\U0001f629')
    # sad_dict.append(u'\U0001F62A')
    # sad_dict.append(u'\U0001F62B')
    # sad_dict.append(u'\U0001F62D')
    # sad_dict.append(u'\U0001F630')
    # sad_dict.append(u'\U0001F631')
    # sad_dict.append(u'\U0001F635')
    # sad_dict.append(u'\U0001F63E')
    # sad_dict.append(u'\U0001F63F')
    # sad_dict.append(u'\U0001F640')
    # sad_dict.append(u'\U0001F645')
    # sad_dict.append(u'\U0001F647')
    # sad_dict.append(u'\U0001f621')
    #
    # char_happy = []
    # for word in happy_dict:
    #     for c in word:
    #         if ord(c) == 55357:
    #             pass
    #         else:
    #             char_happy.append(ord(c))
    # del word
    # del c
    # del happy_dict
    #
    #
    # char_sad = []
    # for word in sad_dict:
    #     for c in word:
    #         if ord(c) == 55357:
    #             pass
    #         else:
    #             char_sad.append(ord(c))
    # del word
    # del c
    # del sad_dict

    # print char_happy
    # print char_sad
    #
    # return (char_happy, char_sad)
    return dict_of_sentiments


def pure_text(text, dict_of_sentiments):

    new_list = []
    words = text.strip().split()
    pattern_http = re.compile('^http')

    for word in words:
        try:
            if word[0] == '@':
                new_list.append('TO_USER')
                pass
            elif word[0] == '#':
                try:
                    new_list.append(word[1:].lower())
                except:
                    pass

            elif pattern_http.match(word) is not None:
                new_list.append('URL')

            else:

                not_letters = re.findall(r'[^a-zA-Z]+', word)
                for each_letter in not_letters:
                    for each_char in each_letter:
                        if ord(each_char) > 50000:
                            if ord(each_char) in dict_of_sentiments:
                                new_list.append(dict_of_sentiments[ord(each_char)])

                            # if ord(each_char) in happy_list:
                            #     new_list.append(u'happy')
                            # elif ord(each_char) in sad_list:
                            #      new_list.append(u'angry')

                word = re.findall(r'[a-zA-Z]+', word)
                for w in word:
                    if w == 'm':
                        w = 'am'
                    new_list.append(w.lower())
        except:
            pass
    print "NEW LIST", new_list
    return " ".join(new_list)  # def connect_to_db():


######################
#Connect to database
#####################
def database(URL, db_name):
    server = couchdb.Server('http://'+URL+':5984/')

    try:
        db = server[db_name]
        return db
    except:
        print "DB not found. Closing"
        sys.exit(2)


if len(sys.argv) != 4:
    sys.stderr.write("Arguments <URL(localhost)> <DB name> <view (test/test)>")
    sys.exit()

URL = sys.argv[1]
name_of_db = sys.argv[2]
view = sys.argv[3]


#### MAIN
LIMIT_OF_DOCUMENTS = 1000;

dict_of_sentiments = dictionaries()

db = database(URL, name_of_db)
while len(db.view(view, limit=LIMIT_OF_DOCUMENTS)) > 0:
    for data in db.view(view, limit=LIMIT_OF_DOCUMENTS):
        print '=' * 40
        print '====>', data['value']
        print '---->', data['value'].split()
        json_data = {}
        json_data = db.get(data['id'])
        # print 'REVISION', db.get(data['id'])['_rev']
        # print json_data['_rev']
        # print json_data['_id']
        testimonial = TextBlob(pure_text(data['value'], dict_of_sentiments))
        polarity_value = testimonial.sentiment.polarity * 100.0
        polarity = ""
        if polarity_value == 0:
            polarity = 'neutral'
        elif polarity_value < 0:
            polarity = 'negative'
        else:
            polarity = 'positive'
        subjectivity = testimonial.sentiment.subjectivity
        json_data['label'] = {'polarity': polarity, 'polarity_value': polarity_value, 'subjectivity': subjectivity}
        db.save(json_data)

    # f = open('input/m/t1.txt', 'r')
    #
    # lines = f.readlines()
    #
    # for line in lines:
    #     print pure_text(line)
    #
    #

    ###############################









    # train = [
    #     ('I love this sandwich.', 'pos'),
    #     ('this is an amazing place!', 'pos'),
    #     ('I feel very good about these beers.', 'pos'),
    #     ('this is my best work.', 'neutral'),
    #     ("what an awesome view", 'pos'),
    #     ('I do not like this restaurant', 'neg'),
    #     ('I am tired of this stuff.', 'neg'),
    #     ("I can't deal with this", 'neg'),
    #     ('mashable', 'neutral'),
    #     ('my boss is horrible.', 'neg')
    # ]
    # test = [
    #     ('the beer was good.', 'pos'),
    #     ('I do not enjoy my job', 'neg'),
    #     ("I ain't feeling dandy today.", 'neg'),
    #     ("I feel amazing!", 'pos'),
    #     ('Gary is a friend of mine.', 'pos'),
    #     ("I can't believe I'm doing this.", 'neg')
    # ]
    #
    # from textblob.classifiers import NaiveBayesClassifier
    # cl = NaiveBayesClassifier(train)
    # prob_dist = cl.prob_classify("I feel sick. Can someone please ban chocolate?")
    # print prob_dist.max()
    #
    # print prob_dist.prob("pos")
    #
    # print prob_dist.prob("neg")
    #
    # print prob_dist.prob("neutral")
    # from nltk.corpus import movie_reviews
    #
    # reviews = [(list(movie_reviews.words(fileid)), category)
    #               for category in movie_reviews.categories()
    #               for fileid in movie_reviews.fileids(category)]
    #
    # new_train, new_test = reviews[0:100], reviews[101:200]
    # print new_train[0]
    #
    # cl.update(new_train)
    # print cl.classify("I feel sick. Can someone please ban chocolate?")