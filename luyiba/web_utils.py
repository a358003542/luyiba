#!/usr/bin/env python
# -*-coding:utf-8-*-

import threading
import logging
import requests
import js2py
from my_fake_useragent import UserAgent
from datetime import datetime
from dateutil.relativedelta import relativedelta

from .cache_utils import cachedb, func_cache
from .datetime_helper import get_timestamp, get_dt_fromtimestamp

logger = logging.getLogger(__name__)

rank_url = 'https://lol.qq.com/act/lbp/common/guides/guideschampion_rank.js'
position_url = 'https://lol.qq.com/act/lbp/common/guides/guideschampion_position.js'
hero_url = 'https://game.gtimg.cn/images/lol/act/img/js/heroList/hero_list.js'

ua = UserAgent(family=['chrome', 'firefox'])


def use_cache_callback_requests_web(cache_data, func, args, kwargs, use_cache_oldest_dt=None):
    timestamp = cache_data.get('timestamp', get_timestamp())
    data_dt = get_dt_fromtimestamp(timestamp)

    if use_cache_oldest_dt is None:
        target_dt = datetime.now() - relativedelta(seconds=14)  # default 14 days
    else:
        target_dt = use_cache_oldest_dt

    if data_dt < target_dt:  # too old then we will re-excute the function
        t = threading.Thread(target=update_requests_web, args=(cache_data, args))
        t.daemon = True
        t.start()


def update_requests_web(cache_data, args):
    logger.info('update_requests_web')
    headers = {
        'user-agent': ua.random()
    }
    url = args[0]
    data = requests.get(url, headers=headers, timeout=30)

    cache_data['data'] = data
    cache_data['timestamp'] = str(get_timestamp())
    key = cache_data.get('key')

    cachedb.set(key, cache_data)
    return data


@func_cache(use_cache_callback=use_cache_callback_requests_web)
def _requests_web(url):
    """
    有数据则直接使用 没有数据则试着从网络上请求
    直接使用数据的时候会根据数据的时间戳来判断新旧，如果数据过旧则启动后台更新线程

    :param url:
    :return:
    """
    headers = {
        'user-agent': ua.random()
    }

    data = requests.get(url, headers=headers, timeout=30)

    return data


@func_cache("position_data")
def download_position_data():
    res = _requests_web(position_url)

    position_data = js2py.eval_js(res.text).to_dict()

    return position_data


@func_cache("rank_data")
def download_rank_data():
    res = _requests_web(rank_url)

    rank_data = js2py.eval_js(res.text).to_dict()

    return rank_data


@func_cache("hero_data")
def download_hero_data():
    """
    :return:
    """
    res = _requests_web(hero_url)

    hero_data = res.json()

    return hero_data


def get_all_hero_name(data=None):
    if not data:
        data = download_hero_data()['hero']
    res = []
    for item in data:
        res.append(item['name'])
    return res


def mix_all_data_togather():
    hero_data = download_hero_data()
    positon_data = download_position_data()
    rank_data = download_rank_data()

    res = []
    for item in hero_data['hero']:
        heroId = item['heroId']

        new_item = item.copy()
        if 'selectAudio' in new_item:
            del new_item['selectAudio']
        if 'banAudio' in new_item:
            del new_item['banAudio']

        new_item['rank_data'] = rank_data['list'].get(str(heroId), {})
        new_item['position_data'] = positon_data['list'].get(str(heroId), {})

        res.append(new_item)

    return res
