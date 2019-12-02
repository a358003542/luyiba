#!/usr/bin/env python
# -*-coding:utf-8-*-

import random
import click
import logging

from luyiba.utils import random_line_safe, mix_all_data_togather, get_all_hero_name, add_mylist, remove_mylist, \
    delete_mylist, get_mylist, explain_it, find_target_by_name, build_stream_function, random_mylist_safe
from luyiba.filter import *

logger = logging.getLogger(__name__)


@click.command()
@click.option('--input', type=click.Path(exists=True), help='指定文本随机模式')
@click.option('-a', '--all', is_flag=True, help='全英雄随机模式')
@click.option('--list', is_flag=True, help='列出全英雄名')
@click.option('--mylist', is_flag=True, help='列出我的喜好英雄清单')
@click.option('--mylist-input', type=click.Path(exists=True), help='根据一行行导入我的喜好清单')
@click.option('--mylist-add', help='我的喜好清单添加一个')
@click.option('--mylist-remove', help='我的喜好清单删除一个')
@click.option('--mylist-delete', is_flag=True, help='我的喜好清单清空')
@click.option('--position', type=click.Choice(['top', 'mid', 'jungle', 'bottom', 'support'], case_sensitive=False),
              help='指定我只想玩那个位置')
@click.option('--role', type=click.Choice(['tank', 'mage', 'support', 'marksman', 'fighter', 'assassin'],
                                          case_sensitive=False), help='指定我只想玩某种角色')
def main(input='', all=False, list=False, mylist=False, mylist_add='', mylist_remove='', mylist_input='',
         mylist_delete=False, position='', role=''):
    """
    英雄联盟随机英雄选择器

    默认根据用户喜好清单随机选择
    """
    if list:
        all_hero_name = get_all_hero_name()
        for name in all_hero_name:
            click.echo(name)
        return
    elif mylist:
        mylist = get_mylist()
        for item in mylist:
            click.echo(item)
        return

    elif mylist_input:
        line = open(mylist_input, encoding='utf8').readlines()
        for item in line:
            item = item.strip()
            if item:
                add_mylist(item)

        return

    elif mylist_add:
        add_mylist(mylist_add)
        return
    elif mylist_remove:
        remove_mylist(mylist_remove)
        return
    elif mylist_delete:
        delete_mylist()
        return

    # 设置过滤逻辑
    all_data = mix_all_data_togather()
    d = {
        'data': all_data,
        'position': position,
        'role': role,
    }
    filter_func = build_stream_function(filter_position, filter_role)
    d = filter_func(d)
    data = d['data']

    if all:
        result = random.choice(data)
        click.echo(explain_it(result))
        return
    elif input:
        target_name = random_line_safe(input, get_all_hero_name(data))
        result = find_target_by_name(all_data, target_name)
        click.echo(explain_it(result))
        return
    # 最后默认从我最喜爱的英雄里面随机抽选
    else:
        target_name = random_mylist_safe(get_all_hero_name(data))
        result = find_target_by_name(all_data, target_name)
        click.echo(explain_it(result))


if __name__ == '__main__':
    main()
