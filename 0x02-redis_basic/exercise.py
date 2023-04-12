#!/usr/bin/env python3

'''
Function that sets data to random keys and returns the key
'''

import uuid
import redis
from typing import Union


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
