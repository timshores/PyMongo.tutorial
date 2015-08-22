import pymongo
import datetime
import sys

# establish a connection to the database
connection = pymongo.MongoClient("mongodb://localhost")

# remove one student
def remove_student(student_id):

    print "removing student document"
    # get a handle to the school database
    db = connection.test
    scores = db.scores

    try:
        result = scores.delete_one( { 'student' : student_id } )
        print "num removed: ", result.deleted_count

    except Exception as e:
        print "Exception: ", type(e), e
        raise

# add a review date to all records
def find_student_data(student_id):

    print "Searching for student data with id = ", student_id
    # get a handle to the school database
    db = connection.test
    scores = db.scores

    try:
        docs = scores.find( {'student':student_id} )
        for doc in docs:
            print doc

    except Exception as e:
        print "Exception: ", type(e), e
        raise

remove_student(3)
find_student_data(3)
