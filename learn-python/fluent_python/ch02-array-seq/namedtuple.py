"""
具名元组
"""
from collections import namedtuple


def use_namedtuple():
    """
    创建一个具名元组需要两个参数，一个是类名，另一个是类的各个字段的名字。后者可
    以是由数个字符串组成的可迭代对象，或者是由空格分隔开的字段名组成的字符串。
    :return:
    """
    City = namedtuple('City', 'name country population coordinates')
    tokyo = City('Tokyo', 'JP', 36.933, (35.689722, 139.691667))
    print(tokyo)
    print(tokyo.population)
    print(tokyo[1])
    print(City._fields)  # _fields 属性是一个包含这个类所有字段名称的元组
    LatLong = namedtuple('LatLong', 'lat long')
    delhi_data = ('Delhi NCR', 'IN', 21.935, LatLong(28.613889, 77.208889))
    delhi = City._make(
        delhi_data)  # 用 _make() 通 过 接 受 一 个 可 迭 代 对 象 来 生 成 这 个 类 的 一 个 实 例， 它 的 作 用 跟City(*delhi_data) 是一样的。
    print(delhi._asdict())  # _asdict() 把具名元组以 collections.OrderedDict 的形式返回，我们可以利用它来把元组里的信息友好地呈现出来。


if __name__ == '__main__':
    use_namedtuple()
