"""
列表推导
"""
from typing import List


def str_to_unicode(string: str = "$¢£¥€¤") -> List[int]:
    """
    把一个字符串变成 Unicode 码位的列表
    :return:  Unicode 码位的列表
    """
    # 第一种方法实现：for循环
    # codes = []
    # for char in string:
    #     codes.append(ord(char))
    # return codes

    # 第二种方法实现：列表推导
    # return [ord(char) for char in string]

    # 第三种方法实现：生成器表达式
    # 在数据量大时，且不是马上需要所有数据时推荐这个
    return list(ord(char) for char in string)


def str_to_unicode1(string: str = "$¢£¥€¤") -> List[int]:
    """
    列表推导同filter和map的比较
    把一个字符串变成 Unicode 码位的列表
    :return:  Unicode 码位的列表
    """
    # 第一种方法实现：列表推导
    # return [ord(char) for char in string if ord(char) > 127]
    # 第二种方法实现：filter和map
    return list(filter(lambda c: c > 127, map(ord, string)))


if __name__ == '__main__':
    print(str_to_unicode())  # 把一个字符串变成 Unicode 码位的列表
    print(str_to_unicode1())  # 列表推导同filter和map的比较
    pass
