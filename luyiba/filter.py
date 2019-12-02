#!/usr/bin/env python
# -*-coding:utf-8-*-


import logging

logger = logging.getLogger(__name__)


def filter_position(d):
    data = d['data']
    position = d.get('position')

    if position:
        new_data = []
        for item_data in data:
            if position in item_data['position_data']:
                new_data.append(item_data)

        d['data'] = new_data
    return d


def filter_role(d):
    data = d['data']
    role = d.get('role')

    if role:
        new_data = []
        for item_data in data:
            if role in item_data['roles']:
                new_data.append(item_data)

        d['data'] = new_data
    return d
