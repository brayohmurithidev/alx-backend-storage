#!/usr/bin/env python3

'''
FIND DOCUMENTS MATCHING TOPIC NAME IN THE ARRAY TOPICS
'''


def schools_by_topic(mongo_collection, topic):
    '''
    Will use operator $all
    '''
    results = mongo_collection.find({'topics': {'$all': [topic]}})
    return results
