#!/usr/bin/env python
# -*-coding:utf-8-*-

import logging

from pywander.cache import get_cachedb
from luyiba import APP_NAME

logger = logging.getLogger(__name__)


MY_FAVORITE_LIST = 'my-favorite-list'

cachedb = get_cachedb(APP_NAME)


def add_mylist(value):
    my_favorite_list = cachedb.get(MY_FAVORITE_LIST, default=set())
    my_favorite_list.add(value)
    cachedb.set(MY_FAVORITE_LIST, my_favorite_list)


def remove_mylist(value):
    my_favorite_list = cachedb.get(MY_FAVORITE_LIST, default=set())
    my_favorite_list.discard(value)
    cachedb.set(MY_FAVORITE_LIST, my_favorite_list)


def delete_mylist():
    cachedb.set(MY_FAVORITE_LIST, set())


def get_mylist():
    my_favorite_list = cachedb.get(MY_FAVORITE_LIST, default=set())

    return list(my_favorite_list)
