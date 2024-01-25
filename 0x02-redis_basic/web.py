#!/usr/bin/env python3
''' implementing an expiring web cache tracker '''
import requests
import redis
from functools import wraps
from typing import Callable

redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)

def cache_with_expiration(expiration_time: int):
    def decorator(method: Callable) -> Callable:
        @wraps(method)
        def wrapper(url: str) -> str:
            count = "count:{}".format(url)
            redis_client.incr(count)
            cache_key = "cache:{}".format(url)
            cached_res = redis_client.get(cache_key)
            
            if cached_res:
                return cached_res.decode('utf-8')
            
            response = requests.get(url)
            html_content = response.text
            
            redis_client.setec(cache_key, expiration_time, html_content)
            
            return html_content
        return wrapper
    return decorator

@cache_with_expiration(expiration_time=10)
def get_page(url: str) -> str:
    ''' Fetch the HTML content of a URL and cache the result '''
    response = requests.get(url)
    return response.text

# example
url = "http://slowwly.robertomurray.co.uk/delay/5000/url/http://www.google.com"
html_content = get_page(url)
print(html_content)