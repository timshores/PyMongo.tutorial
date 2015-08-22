import pymongo
import sys

# establish a connection to the db
connection = pymongo.MongoClient("mongodb://localhost")

def insert_many():

# get a handle to the school db
    db = connection.school
    people = db.people

    print "insert_many, reporting for duty"

    richard = { "name" : "Richard Kreuter", "company" : "MongoDB",
                "interests" : ['horses', 'skydiving', 'fencing']}
    andrew = { "_id" : "erlichson", "name" : "Andrew Erlichson",
                "company" : "MongoDB", "interests" : ['running', 'cycling',
                'photography']}

    people_to_insert = [andrew,richard]

    try:
        people.insert_many(people_to_insert, ordered = True)

    except Exception as e:
        print "Unexpected error: ", type(e), e

def print_people():
    db = connection.school
    people = db.people

    cur = people.find({}, {'name':1})
    for doc in cur:
        print doc


print "Before the insert_many, here are the people"
print_people()
insert_many()
print "\n\nAfter the insert_many, here are the people"
print_people()
