#!/usr/bin/env python
# -*-coding:utf-8-*-

import click
import logging

from luyiba import __version__
from .cache_utils import add_mylist, remove_mylist, delete_mylist, get_mylist
from .web_utils import get_all_hero_name


def print_version(ctx, param, value):
    if not value or ctx.resilient_parsing:
        return
    click.echo(f'luyiba {__version__}')
    ctx.exit()


def enable_debug(ctx, param, value):
    if not value or ctx.resilient_parsing:
        return

    logging.basicConfig(level=logging.DEBUG)


def list_all_hero(ctx, param, value):
    if not value or ctx.resilient_parsing:
        return

    all_hero_name = get_all_hero_name()
    for name in all_hero_name:
        click.echo(name)
    ctx.exit()


def list_my_hero(ctx, param, value):
    if not value or ctx.resilient_parsing:
        return

    mylist = get_mylist()
    if mylist:
        for item in mylist:
            click.echo(item)
    else:
        click.echo('你的个人喜好清单目前为空')

    ctx.exit()


def input_mylist_call(ctx, param, value):
    if not value or ctx.resilient_parsing:
        return

    line = open(value, encoding='utf8').readlines()
    for item in line:
        item = item.strip()
        if item:
            add_mylist(item)
    ctx.exit()


def add_mylist_call(ctx, param, value):
    if not value or ctx.resilient_parsing:
        return

    add_mylist(value)
    click.echo(f'{value} added.')
    ctx.exit()


def remove_mylist_call(ctx, param, value):
    if not value or ctx.resilient_parsing:
        return

    remove_mylist(value)
    click.echo(f'{value} removed.')
    ctx.exit()


def delete_mylist_call(ctx, param, value):
    if not value or ctx.resilient_parsing:
        return

    delete_mylist()
    click.echo(f'your favorite list deleted.')
    ctx.exit()
