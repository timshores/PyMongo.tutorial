import pymongo
import sys

# establish a connection to the db
connection = pymongo.MongoClient("mongodb://localhost")

def lowest_grade():

# get a handle to the reddit db
    db = connection.students
    grades = db.grades

    print "Seeking lowest grade for each student."
    query = {}

    try:
        cursor = grades.find(query)

    except Exception as e:
        print "Unexpected error: ", type(e), e

    current = 0
    for doc in cursor:
        low_score = 10000
        if current == doc.student_id:
            for doc in cursor:
                if doc.type == "homework":
                    if low_score > doc.score:
                        low_score = doc.score
                        low_id = _id



        else:
            current = doc.student_id


lowest_grade()
