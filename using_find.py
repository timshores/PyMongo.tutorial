import pymongo
import sys

# establish connection to the db
connection = pymongo.MongoClient("mongodb://localhost")

# get handle to school db
db = connection.test
scores = db.scores

def find():
    print "find, reporting for duty"
    query = {'type':'exam'}

    try:
        cursor = scores.find(query)

    except Exception as e:
        print "Unexpected error: ", type(e), e

    sanity = 0
    for doc in cursor:
        print doc
        sanity += 1
        if (sanity > 10):
            break



def find_one():

    print "find one, reporting for duty"
    query = {'student':10}

    try:
        doc = scores.find_one(query)

    except Exception as e:
        print "Unexpected error: ", type(e), e

    print doc

find()
