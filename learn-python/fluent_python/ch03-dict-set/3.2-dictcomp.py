"""
列表推导
"""
from collections import defaultdict
DIAL_CODES = [
    (86, 'China'),
    (91, 'India'),
    (1, 'United States'),
    (62, 'Indonesia'),
    (55, 'Brazil'),
    (92, 'Pakistan'),
    (880, 'Bangladesh'),
    (234, 'Nigeria'),
    (7, 'Russia'),
    (81, 'Japan'),
]


def use_dict_comp(tuple_list=None):
    """
    把一个字符串变成 Unicode 码位的列表
    :return:  Unicode 码位的列表
    """
    if tuple_list is None:
        tuple_list = DIAL_CODES
    return {code: country.upper() for country, code in tuple_list.items() if
            code < 66}  # 用区域码作为键，国家名称转换为大写，并且过滤掉区域码大于或等于66 的地区。


if __name__ == '__main__':
    defaultdict(int)
    print(use_dict_comp())  # 把一个字符串变成 Unicode 码位的列表
    pass
