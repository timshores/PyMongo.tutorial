import pymongo
import sys

# add a review date to a single record using update_one
def get_next_sequence_number(name):

    # establish a connection to the database
    connection = pymongo.MongoClient("mongodb://localhost")

    # get a handle to the school database
    db = connection.test
    counters = db.counters

    # let's get a sequence number.
    # note there are two other variants of this call:
        # find_one_and_delete
        # find_one_and_replace
    # all three map to the mongo server command find_and_modify

    try:

        counter = counters.find_one_and_update( filter = { 'type' : name }, update = { '$inc' : { 'value' : 1 } }, upsert = True, return_document = pymongo.ReturnDocument.AFTER )

    except Exception as e:
        print "Exception: ", type(e), e
        raise

    counter_value = counter['value']
    return counter_value

print get_next_sequence_number('pid')
print get_next_sequence_number('pid')
print get_next_sequence_number('pid')
