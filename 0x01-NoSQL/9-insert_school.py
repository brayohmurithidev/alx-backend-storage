#!/usr/bin/env python3


'''
INSERT DOCUMENT BASED ON KWARGS:
'''


def insert_school(mongo_collection, **kwargs):
    '''
    use insert one method
    '''
    document = mongo_collection.insert_one(kwargs).inserted_id
    return document
