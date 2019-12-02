#!/usr/bin/env python
# -*-coding:utf-8-*-


import os

APP_NAME = 'luyiba'

user_data_path = os.path.expanduser(os.path.join('~', 'AppData', 'Roaming', APP_NAME))

if not os.path.exists(user_data_path):
    os.mkdir(user_data_path)

cache_path = os.path.join(user_data_path, 'cache')
