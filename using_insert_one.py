import pymongo
import sys

# establish a connection to the db
connection = pymongo.MongoClient("mongodb://localhost")

def insert():

# get a handle to the reddit db
db = connection.test
scores = db.scores

    print "find with sort/skip/limit, reporting for duty"

    query = {}

    try:
        # this dot syntax can also take place on a single line
        cursor = scores.find(query).skip(4)
        cursor = cursor.limit(3)
        #cursor = cursor.sort('student', pymongo.ASCENDING)
        cursor = cursor.sort([('student',pymong.ASCENDING),('score',pymongo.DESCENDING)])
            # python tuple array needed to describe order of sorting
            # python dictionary doesn't retain order, whereas JSON does
            # so sorting on multiple keys requires array

    except Exception as e:
        print "Unexpected error: ", type(e), e

    for doc in cursor:
        print doc

find()
