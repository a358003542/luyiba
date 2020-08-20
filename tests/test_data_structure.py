#!/usr/bin/env python
# -*-coding:utf-8-*-


from luyiba.web_utils import mix_all_data_togather, download_hero_data


def test_data_structure():
    """
    测试从网络上读取的数据，确保数据结构完整，根据后面的程序要求
    这些字段是必须有的，如果测试未通过则程序会有误。

    [{'heroId': '1', 'name': '黑暗之女', 'alias': 'Annie', 'title': '安妮', 'roles': ['mage'], 'isWeekFree': '0', 'attack': '2', 'defense': '
3', 'magic': '10', 'difficulty': '6', 'isARAMweekfree': '0', 'ispermanentweekfree': '0', 'changeLabel': '无改动', 'rank_data': {'banrate': '36', 'bottom': {'champlanorder': '', 'hold2': '
', 'lanewinrate': '', 'lanshowrate': ''}, 'championid': '1', 'jungle': {'champlanorder': '', 'hold2': '', 'lanewinrate': '', 'lanshowrate': ''}, 'lanes': 'bottom,jungle,mid,support,top',
'mid': {'champlanorder': '6', 'hold2': '-10', 'lanewinrate': '5416', 'lanshowrate': '180'}, 'showrate': '214', 'support': {'champlanorder': '', 'hold2': '', 'lanewinrate': '', 'lanshowrat
e': ''}, 'top': {'champlanorder': '', 'hold2': '', 'lanewinrate': '', 'lanshowrate': ''}, 'winrate': '5404'}, 'position_data': {'mid': '180'}},
    ]

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

        for position in item['position_data']:
            assert 'lanshowrate' in item['rank_data'][position]
            assert 'lanewinrate' in item['rank_data'][position]
            assert 'champlanorder' in item['rank_data'][position]
