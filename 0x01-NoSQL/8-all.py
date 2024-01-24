#!/usr/bin/env python3
''' lists all documents in collection '''


def list_all(mongo_collection):
    ''' listing all the documents in a MongoDB collection'''
    finder = mongo_collection.find({})

    documents = list(finder)

    return documents
