#!/usr/bin/env python3
"""
This module contains a function that returns all
students sorted by average score
"""


def top_students(mongo_collection):
    """
    This function finds the top students and sorts them
    by average score
    Args:
        mongo_collection: a pymongo collection object
    Return:
         sorted average
    """
    top = mongo_collection.aggregate([
        {
            "$project": {
                "name": "$name",
                "averageScore": {"$avg": "$topics.score"}
            }
        },
        {"$sort": {"averageScore": -1}}
    ])
    return top
