#!/usr/bin/env python
# -*-coding:utf-8-*-

import logging
import requests
import js2py
from my_fake_useragent import UserAgent
from .cache_utils import set_cache, get_cache

logger = logging.getLogger(__name__)

rank_url = 'https://lol.qq.com/act/lbp/common/guides/guideschampion_rank.js'
position_url = 'https://lol.qq.com/act/lbp/common/guides/guideschampion_position.js'
hero_url = 'https://game.gtimg.cn/images/lol/act/img/js/heroList/hero_list.js'


def _requests_web(url):
    res = get_cache(url)
    if res:
        logger.info('read data from cache for url: {}'.format(url))
        return res
    else:
        logger.info('update data from web for url: {}'.format(url))
        ua = UserAgent(family=['chrome', 'firefox'])
        headers = {
            'user-agent': ua.random()
        }
        res = requests.get(url, headers=headers, timeout=30)
        set_cache(url, res)
        return res


def download_position_data():
    res = _requests_web(position_url)

    position_data = js2py.eval_js(res.text).to_dict()

    return position_data


def download_rank_data():
    res = _requests_web(rank_url)

    rank_data = js2py.eval_js(res.text).to_dict()

    return rank_data


def download_hero_data():
    """

    :return:
    """
    res = _requests_web(hero_url)

    hero_data = res.json()

    return hero_data
