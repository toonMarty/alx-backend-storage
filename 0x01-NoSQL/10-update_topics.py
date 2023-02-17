#!/usr/bin/env python3
"""
This module contains a function that changes
all topics of a school document based on the name
"""


def update_topics(mongo_collection, name, topics):
    """
    This function updates topics of a school document based
    on the name
    Args:
        mongo_collection: a pymongo collection object
        name (str): the school name to update
        topics (list): list of topics approached in the school
    Return:
         the updated document with topics
    """
    return mongo_collection.update_one({'name': name},
                                       {'$set': {'topics': topics}})
