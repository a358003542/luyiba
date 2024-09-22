#!/usr/bin/env python
# -*-coding:utf-8-*-

import random
import click

from luyiba.command_utils import print_version, list_all_hero, list_my_hero, add_mylist_call, remove_mylist_call, \
    delete_mylist_call, enable_debug
from luyiba.utils import explain_it, find_target_by_name, build_stream_function, random_mylist_safe, \
    position_shortname, role_shortname
from luyiba.filter import *
from luyiba.web_utils import get_all_hero_name, mix_all_data_togather

logger = logging.getLogger(__name__)


@click.command()
@click.option('-v', '--version', is_flag=True, callback=print_version, expose_value=False, is_eager=True, help='本软件版本')
@click.option('-V', '--verbose', is_flag=True, is_eager=True, callback=enable_debug, expose_value=False, help='打印输出冗余信息')
@click.option('-l', '--list', is_flag=True, help='列出全英雄名', is_eager=True, callback=list_all_hero, expose_value=False)
@click.option('-m', '--mode', default='all', show_default=True, help='模式： all 全英雄随机 mylist 我的喜好清单随机 rank 排名列出模式')
@click.option('--rank', default='hot', show_default=True, type=click.Choice(['hot', 'ban', 'show', 'win'], case_sensitive=False), help='根据什么排名，默认热门率')
@click.option('-n', '--name', help='指定英雄名字选取模式')
@click.option('--number', default=5, type=int, show_default=True, help='rank模式下显示数目')
@click.option('-p', '--position', type=click.Choice(['top', 'mid', 'jungle', 'bottom', 'support',
                                                     't', 'm', 'j', 'b', 's'], case_sensitive=False),
              help='指定我只想玩那个位置')
@click.option('-r', '--role', type=click.Choice(['tank', 'mage', 'support', 'marksman', 'fighter', 'assassin',
                                                 't', 'g', 's', 'k', 'f', 'a'],
                                                case_sensitive=False), help='指定我只想玩某种角色')
@click.option('--mylist-list', is_flag=True, help='列出我的喜好英雄清单', is_eager=True, callback=list_my_hero,
              expose_value=False)
@click.option('--mylist-add', help='我的喜好清单添加一个', is_eager=True, callback=add_mylist_call, expose_value=False)
@click.option('--mylist-remove', help='我的喜好清单删除一个', is_eager=True, callback=remove_mylist_call, expose_value=False)
@click.option('--mylist-delete', is_flag=True, help='我的喜好清单清空', is_eager=True, callback=delete_mylist_call,
              expose_value=False)
def main(mode='all', position='', role='', name='', rank='hot', number=5):
    """
    英雄联盟辅助小工具
    """
    # 获取数据和设置过滤逻辑
    all_data = mix_all_data_togather()

    position = position_shortname(position)
    role = role_shortname(role)

    d = {
        'data': all_data,
        'position': position,
        'role': role,
    }
    filter_func = build_stream_function(filter_position, filter_role)
    d = filter_func(d)
    data = d['data']

    # 如果指定name
    if name:
        result = find_target_by_name(all_data, name)
        click.echo(explain_it(result))
        return

    # 工作模式
    if mode == 'all':
        if not data:
            click.echo('找不到数据！')
            return

        result = random.choice(data)
        click.echo(explain_it(result))
        return

    elif mode == 'mylist':
        target_name = random_mylist_safe(get_all_hero_name(data))

        if target_name:
            result = find_target_by_name(all_data, target_name)
            click.echo(explain_it(result))
        else:
            click.echo('从我最喜爱的英雄里面没有找到数据。')
        return

    elif mode == 'rank':
        # 排序
        if rank == 'ban':
            data = sorted(data, key=lambda item: int(
                item['rank_data']['banrate']), reverse=True)
        elif rank == 'show':
            data = sorted(data, key=lambda item: int(
                item['rank_data']['showrate']), reverse=True)
        elif rank == 'win':
            data = sorted(data, key=lambda item: int(
                item['rank_data']['winrate']), reverse=True)
        elif rank == 'hot':
            data = sorted(
                data, key=lambda item: item['rank_data']['hotrate'], reverse=True)

        for item in data[:number]:
            click.echo(explain_it(item))

        return


if __name__ == '__main__':
    main()
