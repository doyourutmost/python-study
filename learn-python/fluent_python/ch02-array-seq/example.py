"""
列表推导和生成器表达式
"""
import array

from fluent_python.util.base_util import println


@println
def example2_1(string: str = "$¢£¥€¤") -> list:
    """
    把一个字符串变成 Unicode 码位的列表
    """
    codes = []
    for char in string:
        codes.append(ord(char))
    return codes


@println
def example2_2(string: str = "$¢£¥€¤") -> list:
    """
    把一个字符串变成 Unicode 码位的列表
    第二种方法实现：列表推导
    使用准则：只用列表推导来创建新的列表，并且尽量保持简短
    """
    return [ord(char) for char in string]


@println
def example2_3_1(string: str = "$¢£¥€¤") -> list:
    """
    把一个字符串变成 Unicode 码位的列表
    用列表推导和 map/filter 组合来创建同样的表单
    """
    return [ord(char) for char in string if ord(char) > 127]


@println
def example2_3_2(string: str = "$¢£¥€¤") -> list:
    """
    把一个字符串变成 Unicode 码位的列表
    用列表推导和 map/filter 组合来创建同样的表单
    """
    return list(filter(lambda c: c > 127, map(ord, string)))


@println
def example2_5_1(string: str = "$¢£¥€¤"):
    """
    用生成器表达式初始化元组
    1、如果生成器表达式是一个函数调用过程中的唯一参数，那么不需要额外再用括号把它围起来。
    2、array 的构造方法需要两个参数，因此括号是必需的。array 构造方法的第一个参数指定了数组中数字的存储方式
    """
    return tuple(ord(char) for char in string)


@println
def example2_5_2(string: str = "$¢£¥€¤"):
    """
    用生成器表达式初始化数组
    """
    return array.array('I', (ord(symbol) for symbol in string))


if __name__ == '__main__':
    # 列表推导的作用只有一个：生成列表。如果想生成其他类型的序列，生成器表达式就派上了用场
    example2_1()
    example2_2()

    # 列表推导同filter和map的比较
    example2_3_1()
    example2_3_2()

    # 生成器表达式
    example2_5_1()
