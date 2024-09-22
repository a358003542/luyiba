
import pytest
import os


def test_load_config():
    from pywander.config import config

    assert config['APP_NAME'] == 'luyiba'

