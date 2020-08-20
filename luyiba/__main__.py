#!/usr/bin/env python
# -*-coding:utf-8-*-

import random
import click

from luyiba.command_utils import print_version, list_all_hero, list_my_hero, input_mylist_call, add_mylist_call, \
    remove_mylist_call, delete_mylist_call, enable_debug
from luyiba.utils import random_line_safe, explain_it, find_target_by_name, build_stream_function, random_mylist_safe, \
    position_shortname, role_shortname
from luyiba.filter import *
from luyiba.web_utils import get_all_hero_name, mix_all_data_togather

logger = logging.getLogger(__name__)


@click.command()
@click.option('-v', '--version', is_flag=True, callback=print_version, expose_value=False, is_eager=True, help='本软件版本')
@click.option('-V', '--verbose', is_flag=True, is_eager=True, callback=enable_debug, expose_value=False, help='打印输出冗余信息')
@click.option('-l', '--list', is_flag=True, help='列出全英雄名', is_eager=True, callback=list_all_hero, expose_value=False)
@click.option('--mylist-list', is_flag=True, help='列出我的喜好英雄清单', is_eager=True, callback=list_my_hero,
              expose_value=False)
@click.option('--mylist-input', type=click.Path(exists=True), help='读取文本导入我的喜好清单', is_eager=True,
              callback=input_mylist_call, expose_value=False)
@click.option('--mylist-add', help='我的喜好清单添加一个', is_eager=True, callback=add_mylist_call, expose_value=False)
@click.option('--mylist-remove', help='我的喜好清单删除一个', is_eager=True, callback=remove_mylist_call, expose_value=False)
@click.option('--mylist-delete', is_flag=True, help='我的喜好清单清空', is_eager=True, callback=delete_mylist_call,
              expose_value=False)
@click.option('-i', '--input', type=click.Path(exists=True), help='指定文本随机模式')
@click.option('-a', '--all', is_flag=True, help='全英雄随机模式')
@click.option('-m', '--mylist', is_flag=True, help='个人喜好清单随机模式')
@click.option('-p', '--position', type=click.Choice(['top', 'mid', 'jungle', 'bottom', 'support',
                                                     't', 'm', 'j', 'b', 's'], case_sensitive=False),
              help='指定我只想玩那个位置')
@click.option('-r', '--role', type=click.Choice(['tank', 'mage', 'support', 'marksman', 'fighter', 'assassin',
                                                 't', 'g', 's', 'k', 'f', 'a'],
                                                case_sensitive=False), help='指定我只想玩某种角色')
def main(input='', all=False, mylist=False, position='', role=''):
    """
    英雄联盟随机英雄选择器

    默认全英雄随机选择，你可以设置为自己喜好的清单随机选择。
    """
    # 设置过滤逻辑
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

    mode = 'all'  # default mode is all
    if mylist:
        mode = 'mylist'
    if input:
        mode = 'input'

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
    elif mode == 'input':
        target_name = random_line_safe(input, get_all_hero_name(data))
        result = find_target_by_name(all_data, target_name)
        click.echo(explain_it(result))
        return


if __name__ == '__main__':
    main()
