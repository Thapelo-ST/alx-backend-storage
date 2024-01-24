#!/usr/bin/env python3
''' changes all topics of a school document based on name '''


def update_topics(mongo_collection, name, topics):
    ''' changing topics based on names '''
    result = mongo_collection.update_one(
        {'name': name},
        {'$set': {'topics': topics}}
    )

    return result.modified_count > 0
