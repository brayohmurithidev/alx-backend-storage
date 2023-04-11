#!/usr/bin/env python3


'''
Listing all documents in a collection
'''


def list_all(mongo_collection):
    '''
    find all documents in the collection
    '''
    documents = mongo_collection.find({})

    # if no documents are found, return an empty list
    if mongo_collection.count_documents({}) == 0:
        return []

    # create a list of all documents
    all_documents = [doc for doc in documents]

    # return the list of all documents
    return all_documents
