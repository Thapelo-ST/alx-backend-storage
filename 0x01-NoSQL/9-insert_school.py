#!/usr/bin/env python3
''' inserts a new document and returns a _id '''


def insert_school(mongo_collection, **kwargs):
    ''' inserting a new document, returning Id '''
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
