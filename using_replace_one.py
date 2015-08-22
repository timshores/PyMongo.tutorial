import pymongo
import datetime
import sys

# establish a connection to the database
connection = pymongo.MongoClient("mongodb://localhost")

# add a review date to a single record using update_one
def remove_all_review_dates():

    print "\n\nremoving all review dates."
    # get a handle to the school database
    db = connection.test
    scores = db.scores

    try:
        # get the doc
        result = scores.update_many({ 'review_date' : { '$exists' : True } }, { '$unset' : { 'review_date' : 1 } } )
        print "Matched this number of documents: ", result.matched_count

    except Exception as e:
        print "Unexpected error: ", type(e), e
        raise

# add a review date to a single record using update_one
def add_review_date_using_replace_one(student_id):

    print "updating record using replace_one"

    # get a handle to the school database
    db = connection.test
    scores = db.scores

    try:
        # get the doc
        score = scores.find_one( { 'student' : student_id, 'type' : 'essay' } )
        print "before: ", score

        # add a review_date
        score['review_date'] = datetime.datetime.utcnow()

        # update using set
        record_id = score['_id']
        scores.replace_one( { '_id' : record_id }, score)

        score = scores.find_one( { '_id' : record_id } )
        print "after: ", score

    except Exception as e:
        print "Unexpected error: ", type(e), e
        raise

# add a review date to sign
def add_review_dates_for_all():

    print "updating all records using update_one and $set"
    # get a handle to the school database
    db = connection.test
    scores = db.scores

    try:
        # update all the docs
        result = score = scores.update_many( {}, { '$set' : { 'review_date' : datetime.datetime.utcnow() } } )
        print "num matched: ", result.matched_count

    except Exception as e:
        raise

#add_review_dates_for_all()
remove_all_review_dates()
add_review_date_using_replace_one(1)
