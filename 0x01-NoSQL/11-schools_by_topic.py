#!/usr/bin/env python3
"""
This module contains a function that returns the list of schools
having a specific topic
"""


def schools_by_topic(mongo_collection, topic):
    """
    This function returns schools which have a specific
    topic
    Args:
        mongo_collection: a pymongo collection object
        topic: the topic searched
    Return:
        list of schools having a specific topic
    """
    return mongo_collection.find({'topics': topic})
