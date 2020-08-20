#!/usr/bin/env python
# -*-coding:utf-8-*-
import time
from datetime import datetime


def get_timestamp():
    """
    获得当前的timestamp
    :return:
    """
    timestamp = time.time()

    return int(timestamp)


def dt_to_timestamp(dt):
    timestamp = dt.timestamp()

    return int(timestamp)


def get_dt_fromtimestamp(timestamp, utc=False):
    """
    根据timestamp获得对应的datetime对象
    """

    if isinstance(timestamp, str):
        timestamp = float(timestamp)

    if utc:
        dt = datetime.utcfromtimestamp(timestamp)
    else:
        dt = datetime.fromtimestamp(timestamp)

    return dt