import pymongo
import sys

# establish a connection to the db
connection = pymongo.MongoClient("mongodb://localhost")

# get a handle to the reddit db
db = connection.reddit
stories = db.stories

def find():

    print "find with regex, reporting for duty"

    query = { 'title' :
        { '$regex' : 'apple|google|microsoft|amazon', '$options' : 'i' }
        }
    projection = { 'title' : 1, '_id' : 0 }

    try:
        cursor = stories.find(query, projection)

    except Exception as e:
        print "Unexpected error: ", type(e), e

    for doc in cursor:
        print doc

find()
