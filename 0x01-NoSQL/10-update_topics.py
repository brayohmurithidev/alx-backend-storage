#!/usr/bin/env python3

'''
UPDATES SCHOOL TOPIC BASED ON NAME
'''


def update_topics(mongo_collection, name, topics):
    '''
    UPDATING TO A STRING OF TOPICS
    '''
    update = mongo_collection.update_many({"name": name},
                                          {'$set': {'topics': topics}})
    return update.upserted_id
