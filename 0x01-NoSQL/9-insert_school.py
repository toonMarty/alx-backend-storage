#!/usr/bin/env python3
"""This module contains a function that inserts a new document
in a collection based on kwargs
"""


def insert_school(mongo_collection, **kwargs):
    """
    This function inserts a document in a collection
    Args:
        mongo_collection: a pymongo collection instance
        kwargs: a dictionary that contains document data
    Return:
         the new _id
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
