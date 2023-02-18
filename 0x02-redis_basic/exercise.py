#!/usr/bin/env python3
"""
This module contains a class, Cache
"""
import redis
import uuid
from typing import Union


class Cache:
    """
    This is the class definition of the Cache class
    It has a constructor and a store method
    """
    def __init__(self):
        """
        This method stores an instance of the Redis client
        as a private variable named _redis
        """
        _redis = redis.Redis()
        _redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        This method takes a data argument and returns a string.
        The method generates a random key, store the input data
        in Redis using the random key
        Args:
            data: the data to be stored
        Return:
             key(str): the key that holds the value of data
        """
        key = str(uuid.uuid4())  # generate a random key
        value = data
        redis_instance = redis.Redis()
        redis_instance.set(key, value)
        return key
