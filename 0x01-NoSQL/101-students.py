#!/usr/bin/env python3
''' returns top students by score '''


def top_students(mongo_collection):
    ''' returnig all students sorted by avarage score '''
    pipeline = [
        {
            "$project": {
                "name": "$name",
                "averageScore": {"$avg": "$topics.score"}
            }
        },
        {"$sort": {"avarageScore": -1}}
    ]

    result = mongo_collection.aggregate(pipeline)

    return result
