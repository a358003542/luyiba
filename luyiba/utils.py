#!/usr/bin/env python
# -*-coding:utf-8-*-

import random
from functools import reduce

from .cache_utils import get_mylist


def random_line(input):
    line = random.choice(open(input, encoding='utf8').readlines())
    if line:
        return line
    else:
        return random_line(input)


def random_mylist_safe(hero_name_list):
    my_list = get_mylist()
    if my_list:
        target_name = random.choice(my_list)
        if target_name and target_name in hero_name_list:
            return target_name
        else:
            return random_mylist_safe(hero_name_list)
    else:
        return ''


def random_line_safe(input, hero_name_list):
    file_list = open(input, encoding='utf8').readlines()
    file_list = [line.strip() for line in file_list]
    line = random.choice(file_list)
    if line and (line in hero_name_list):
        return line
    else:
        return random_line_safe(input, hero_name_list)


def num_file(input):
    length = len(open(input, encoding='utf8').readlines())
    return length


def build_stream_function(*funcs):
    """
    构建流处理函数 函数参数更严格 只接受一个参数 d 字典值
    函数执行的顺序是从左到右
    :param funcs:
    :return:
    """

    return reduce(lambda f, g: lambda d: g(f(d)), funcs)


def position_translation(name):
    ref_dict = {
        'bottom': '下路',
        'support': '辅助',
        'mid': '中单',
        'jungle': '打野',
        'top': '上单'
    }
    return ref_dict[name]


def position_shortname(shortname):
    """
    position缩写名支持
    :param shortname:
    :return:
    """
    ref_dict = {
        't': 'top',
        'm': 'mid',
        'j': 'jungle',
        'b': 'bottom',
        's': 'support'
    }
    if shortname in ref_dict:
        return ref_dict[shortname]
    else:
        return shortname


def role_shortname(shortname):
    """
    role缩写支持
    :param shortname:
    :return:
    """
    ref_dict = {
        't': 'tank',
        'g': 'mage',
        's': 'support',
        'k': 'marksman',
        'f': 'fighter',
        'a': 'assassin'
    }
    if shortname in ref_dict:
        return ref_dict[shortname]
    else:
        return shortname


def role_translation(name):
    ref_dict = {
        'tank': '坦克',
        'mage': '法师',
        'support': '辅助',
        'marksman': '射手',
        'fighter': '战士',
        'assassin': '刺客'
    }
    return ref_dict[name]


def explation_position_rank_data(position, rank_data):
    """
    解释英雄排位数据
    lanshowrate 登场率
    lanewinrate 胜率
    champlanorder 排名

    """
    target_rank_data = rank_data[position]
    text = f"{position_translation(position)}【登场率为 {int(target_rank_data['lanshowrate']) * 0.01:.2f}%】 胜率是 {int(target_rank_data['lanewinrate']) * 0.01:.2f}% 排名第{target_rank_data['champlanorder']}名"
    return text


def explain_position(position_data, rank_data):
    text = ''
    count = 0

    for k, v in sorted(position_data.items(), key=lambda d: int(d[1]), reverse=True):
        if count >= 2:
            break

        line = ''
        if count >= 1:
            line += '此外他还作为'
        else:
            line += '他主要作为'

        line += explation_position_rank_data(k, rank_data=rank_data)
        text += line

        text += '\n'

        # last
        count += 1

    return text


def explain_it(item):
    return f"""你选中的是英雄 {item['name']} {item['title']} 英文名: {item['alias']} 
他是一个 {'和'.join([role_translation(name) for name in item['roles']])} 
他的操作难度是 {item['difficulty']} 【满分10】
{explain_position(item['position_data'], item['rank_data'])}
"""


def find_target_by_name(all_data, name):
    for item in all_data:
        if item['name'] == name:
            return item
