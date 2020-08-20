#!/usr/bin/env python
# -*-coding:utf-8-*-

"""
测试click命令行接口
"""

from click.testing import CliRunner
from luyiba.__main__ import main


def test_main_command():
    runner = CliRunner()
    result = runner.invoke(main)

    assert result.exit_code == 0

    result = runner.invoke(main, ['-l'])
    assert result.exit_code == 0

    result = runner.invoke(main, ['--mylist-list'])
    assert result.exit_code == 0
    result = runner.invoke(main, ['-m'])
    assert result.exit_code == 0

    result = runner.invoke(main, ['-p', 't'])
    assert result.exit_code == 0

    result = runner.invoke(main, ['-p', 't', '-r', 't'])
    assert result.exit_code == 0

    result = runner.invoke(main, ['--version'])
    assert result.exit_code == 0
    assert result.output == 'luyiba 0.3.0\n'
