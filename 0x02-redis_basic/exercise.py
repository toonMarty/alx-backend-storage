#!/usr/bin/env python3
"""
This module contains a class, Cache
"""
import redis
import uuid
from typing import Union, Optional, Callable
import functools


def count_calls(method: Callable) -> Callable:
    """
    This function counts how many times a
    function has been called. This function
    will then be used as a decorator in
    the store method of Cache class
    Args:
        method (Callable): the method which has been called
    Return:
        increment(Callable): a wrapper function that
        handles the counting
    """
    @functools.wraps(method)
    def increment(self, *args):
        """The increment wrapper function"""
        name = method.__qualname__
        result = self._redis.incr(name, amount=1)
        return result
    return increment


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
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
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
        self._redis.set(key, value)
        return key

    def get(self, key: str,
            fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
        """
        This method takes a key string argument and an optional
        Callable argument named fn
        Args:
            key: the key that holds data
            fn: a callable used to convert the data back to the desired format
        Return:
             value(str, bytes, int, float): the value
        """
        value = self._redis.get(key)

        if fn:
            value = fn(value)
        return value

    def get_str(self, key: str) -> str:
        """
        This method automatically parameterizes Cache.get
        with a string conversion method
        Args:
            key: the key that holds data
        Return:
             data(int) as a string decoded using utf-8
        """
        value = self._redis.get(key)
        return value.decode('utf-8')

    def get_int(self, key: str) -> int:
        """
        This method automatically parameterizes Cache.get
        with an int conversion method
        Args:
            key: the key that holds data
        Return:
            data as an int decoded using utf-8
        """
        value = self._redis.get(key)
        try:
            value = int(value.decode('utf-8'))
        except Exception:
            value = 0
        return value
