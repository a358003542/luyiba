#!/usr/bin/env python
# -*-coding:utf-8-*-


from diskcache import Cache
from .config import cache_path

cache = Cache(cache_path)


def set_cache(key, value):
    """
    过期时间 10天
    :param key:
    :param value:
    :return:
    """
    cache.set(key, value, expire=864000)


def get_cache(key):
    return cache.get(key)


MY_FAVORITE_LIST = 'my-favorite-list'
