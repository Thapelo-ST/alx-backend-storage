#!/usr/bin/env python3
''' 
    class that stores an instance of a redis client
    as a private variable and impliments a store method
'''
import redis
import uuid
from typing import Union, Callable
from functools import wraps

def count_calls(method: Callable = None) -> Callable:
    ''' count calls of the cache '''
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper

def call_history(method: Callable = None) -> Callable:
    ''' count calls of the cache '''
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        key = method.__qualname__
	inputs_key = "{}:inputs".format(key)
	outputs_key = "{}:outputs".format(key)
	self._redis.rpush(inputs_key, str(args))
	output = method(self, *args, **kwargs)
	self._redis.rpush(outputs_key, str(output))
        return output
    return wrapper


class Cache:
    ''' class storing instance of redis client '''

    def __init__(self):
        ''' inititialising the class '''
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
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
        return self.get(key, fn=lambda x: int(x) if x else None) 
