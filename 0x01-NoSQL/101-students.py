#!/usr/bin/env python3

'''
function returning students sorted by average score
we use aggregate and $divide operator
'''


def top_students(mongo_collection):
    '''
    Function uses pipeline to return students sorted by average score
    '''
    pipeline = [
        {"$unwind": "$topics"},
        {"$group": {
            "_id": "$_id",
            "name": {"$first": "$name"},
            "total_score": {"$sum": "$topics.score"},
            "num_scores": {"$sum": 1}
        }},
        {"$project": {
            "name": 1,
            "averageScore": {"$divide": ["$total_score", "$num_scores"]}
        }},
        {"$sort": {"averageScore": -1}}
    ]
    results = mongo_collection.aggregate(pipeline)
    return results
