#!/usr/bin/env python
# -*-coding:utf-8-*-

import pytest
from luyiba.web_utils import mix_all_data_togather, download_hero_data, download_position_data, download_rank_data


def test_position_data():
    position_data = download_position_data()

    assert position_data['list']


def test_rank_data():
    """
    """
    rank_data = download_rank_data()
    assert rank_data['list']


def test_data_structure():
    """
    测试从网络上读取的数据，确保数据结构完整，根据后面的程序要求
    这些字段是必须有的，如果测试未通过则程序会有误。

    {'heroId': '1', 'name': '黑暗之女', 'alias': 'Annie', 'title': '安妮', 'roles': ['mage', 'support'], 
    'isWeekFree': '0', 'attack': '2', 'defense': '3', 'magic': '10', 'difficulty': '6', 'isARAMweekfree': '0', 'ispermanentweekfree': '0', 'changeLabel': '无改动', 
    'goldPrice': '450', 'couponPrice': '1000', 'camp': '', 'campId': '', 'keywords': '安妮,黑暗之女,火女,Annie,anni,heianzhinv,huonv,an,hazn,hn', 
    'instance_id': '0b95894e-0df2-470e-b282-6c5f5cf41955', 
    'rank_data': 
        {'championid': '1', 'winrate': '5250', 'showrate': '140', 'banrate': '25', 'lanes': 'bottom,mid,support,top', 
        'bottom': {'lanewinrate': '', 'lanshowrate': '', 'champlanorder': '', 'hold2': ''}, 
        'mid': {'lanewinrate': '5295', 'lanshowrate': '123', 'champlanorder': '13', 'hold2': '-2'}, 
        'support': {'lanewinrate': '', 'lanshowrate': '', 'champlanorder': '', 'hold2': ''}, 
        'top': {'lanewinrate': '', 'lanshowrate': '', 'champlanorder': '', 'hold2': ''}}, 
        'position_data': {'mid': '123'}}

    """
    hero_data = download_hero_data()
    assert 'hero' in hero_data
    for item in hero_data['hero']:
        assert 'heroId' in item

    data = mix_all_data_togather()

    for item in data:
        assert 'name' in item
        assert 'alias' in item
        assert 'title' in item

        assert 'roles' in item
        assert 'difficulty' in item
        assert 'rank_data' in item
        assert 'position_data' in item
        assert 'difficulty' in item

        assert 'winrate' in item['rank_data']
        assert 'showrate' in item['rank_data']
        assert 'banrate' in item['rank_data']

        for position in item['position_data']:
            assert 'lanshowrate' in item['rank_data'][position]
            assert 'lanewinrate' in item['rank_data'][position]
            assert 'champlanorder' in item['rank_data'][position]
