#!/usr/bin/env python3

'''
Function that sets data to random keys and returns the key
'''

import uuid
import redis
from typing import Union, Callable


class Cache:
    '''
    MAP REDIS INSTANCE TO PRIVATE VARIABLE _redis
    '''
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
    '''
    A get method that takes in an optional callable fn
    if the result is None, we return None as well. Otherwise,
    we check if fn is not None and if so, we apply fn to the data.
    Finally, we return the data, which will be a str, bytes, int, or float.
    '''
    def get(self, key: str,
            fn: Callable = None) -> Union[str, bytes, int, float, None]:
        data = self._redis.get(key)
        if data is None:
            return None
        if fn is not None:
            data = fn(data)
        return data

    '''
    We also implement two convenience methods get_str
    and get_int that call get with the appropriate conversion
    function (decode('utf-8') for strings and int() for integers).
    '''
    def get_str(self, key: str) -> Union[str, None]:
        return self.get(key, fn=lambda d: d.decode('utf-8'))

    def get_int(self, key: str) -> Union[int, None]:
        return self.get(key, fn=int)
