import pymongo
import sys

# establish connection to the db
connection = pymongo.MongoClient("mongodb://localhost")

# get handle to school db
db = connection.test
scores = db.scores

def find():
    print "find with projection, reporting for duty"
    query = {'type':'exam'}
    projection = {'student':1, '_id':0}

    try:
        cursor = scores.find(query, projection)

    except Exception as e:
        print "Unexpected error: ", type(e), e

    sanity = 0
    for doc in cursor:
        print doc
        sanity += 1
        if (sanity > 10):
            break

find()
