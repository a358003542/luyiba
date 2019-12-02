#!/usr/bin/env python
# -*-coding:utf-8-*-


def test_data_structure():
    from luyiba.utils import mix_all_data_togather
    data = mix_all_data_togather()

    for item in data:
        assert 'name' in item
        assert 'roles' in item
        assert 'rank_data' in item
        assert 'position_data' in item
        assert 'difficulty' in item
