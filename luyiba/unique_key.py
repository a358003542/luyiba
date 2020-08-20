#!/usr/bin/env python
# -*-coding:utf-8-*-

from collections import OrderedDict
from hashlib import md5
from urllib.parse import urlencode


def build_unique_key(base_key, *args, **kwargs):
    """
    缓存唯一id标识生成函数

    :param base_key: 基本的区分key值 比如函数名
    :param args: 必填参数
    :param kwargs: 其他参数
    :return:
    """
    args_id = ""
    kwargs_id = ""

    if args:
        args_id = '_'.join(args)

    if kwargs:
        kwargs = OrderedDict(sorted(kwargs.items(), key=lambda t: t[0]))
        kwargs_id = urlencode(kwargs)

    key = '_'.join([i for i in [base_key, args_id, kwargs_id] if i])

    key = md5(key.encode()).hexdigest()
    return key