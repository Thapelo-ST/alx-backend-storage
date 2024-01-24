#!/usr/bin/env python3
''' 
    class that stores an instance of a redis client
    as a private variable and impliments a store method
'''
import redis
import uuid
from typing import Union, Callable


class Cache:
    ''' class storing instance of redis client '''

    def __init__(self):
        ''' inititialising the class '''
        self._redis = redis.Redis()
        self._redis.flushdb()
    
    def store(self, data: Union[str, bytes, int, float]) -> str:
        ''' takes data and returns a string key'''
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Callable = None):
        ''' takes arguments, and coverts them in a desired format '''
        data = self._redis.get(key)
        return fn(data) if fn else data

    def get_str(self, key: str) -> str:
        ''' parametarise cache.get and converts it into a string '''
        return self.get(key, fn=lambda x: x.decode('utf-8'))
    
    def get_int(self, key: str) -> int:
        ''' parameetarise cache.get and converts it into an int '''
        return self.get(key, fn=lambda x: int(x) if x else None 
