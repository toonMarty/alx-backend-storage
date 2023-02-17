#!/usr/bin/env python3
"""This module contains a function that lists all documents
in a collection"""


def list_all(mongo_collection):
    """
    This function lists all documents in a collection
    Args:
        mongo_collection: a pymongo collection object
    Return:
         The documents found in a collection if not empty
            else return an empty list
    """
    if mongo_collection is not None:
        return mongo_collection.find()
    return []
