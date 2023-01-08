# -*- encoding: utf-8 -*-
# @File: base_util.py
# @Author: doyourbest
# @Time: 2023/01/07 13:50
from functools import wraps


def println(func):
    @wraps(func)
    def _println(*args, **kwargs):
        result = func(*args, **kwargs)
        print('%s:' % func.__name__, result)

    return _println
