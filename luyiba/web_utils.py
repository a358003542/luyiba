#!/usr/bin/env python
# -*-coding:utf-8-*-

import logging

from pywander.crawler.js_file_loader import js_file_loader
from pywander.crawler.cache_utils import func_cache
from pywander.crawler.web_utils import requests_web

logger = logging.getLogger(__name__)

rank_url = 'https://lol.qq.com/act/lbp/common/guides/guideschampion_rank.js'
position_url = 'https://lol.qq.com/act/lbp/common/guides/guideschampion_position.js'
hero_url = 'https://game.gtimg.cn/images/lol/act/img/js/heroList/hero_list.js'


@func_cache("position_data")
def download_position_data():
    res = requests_web(position_url)

    position_data = js_file_loader(res.text)

    # 为了保证和旧版本缓存数据兼容
    position_data = position_data['CHAMPION_POSITION']

    return position_data


@func_cache("rank_data")
def download_rank_data():
    res = requests_web(rank_url)

    rank_data = js_file_loader(res.text)

    # 为了保证和旧版本缓存数据兼容
    rank_data = rank_data['CHAMPION_RANK']

    return rank_data


@func_cache("hero_data")
def download_hero_data():
    """
    :return:
    """
    res = requests_web(hero_url)

    hero_data = res.json()

    return hero_data


def get_all_hero_name(data=None):
    if not data:
        data = download_hero_data()['hero']
    res = []
    for item in data:
        res.append(item['name'])
    return res


def add_hot_rate(data):
    """
    """
    new_data = []

    for item in data:
        new_item = item.copy()
        rank_data = new_item['rank_data']
        hotrate = int(rank_data['banrate']) + int(rank_data['showrate'])
        rank_data['hotrate'] = hotrate
        new_data.append(new_item)

    return new_data


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

    res = add_hot_rate(res)

    return res
