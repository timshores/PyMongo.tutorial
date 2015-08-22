import pymongo
import sys

# homework 3.1
# establish a connection to the db
connection = pymongo.MongoClient("mongodb://localhost")
# get a handle to the database
db = connection.school
students = db.students

def remove_lowest():

    pipeline = [
        { '$match' : { 'scores.type' : 'homework' } },
        { '$unwind' : '$scores' },
        { '$match' : { 'scores.type' : 'homework' } },
        { '$sort' : { '_id' : pymongo.ASCENDING, 'scores.score' : pymongo.ASCENDING } }
    ]
    # this aggregation treats each array element as a separate document
    cursor = students.aggregate(pipeline)

    student_id = -1;

    for item in cursor:

        if (item['_id'] != student_id):

            students.update( { '_id' : item['_id'] }, { '$pull' : { 'scores' : { 'score' : item['scores']['score'] } } } )

        student_id = item['_id']


remove_lowest()
