# -*- encoding: utf-8 -*-
# @File: logger.py
# @Author: doyourbest
# @Time: 2023/01/05 21:32
import math
import time
from functools import wraps
from typing import List


def logger(func):
    @wraps(func)
    def clocked(*args):
        t0 = time.time()
        result = func(*args)
        elapsed = time.time() - t0
        func_name = func.__name__
        (arr_data,) = args
        data = math.log10(len(arr_data))

        if check_order(result) is False:
            raise Exception('列表乱序')

        print('{} 算法排序 10^{:.1f} 数据量耗时: {:.2f} 秒'.format(func_name, data, elapsed))
        return result

    return clocked


def check_order(arr: List[int]) -> bool:
    """
    校验数组是否有序
    :param arr:
    :return: 数组是否有序
    """
    for i in range(1, len(arr)):
        if arr[i] < arr[i - 1]:
            return False
    return True
