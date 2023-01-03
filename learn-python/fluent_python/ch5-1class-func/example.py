from typing import List


def example5_9() -> List[str]:
    """列出常规对象没有而函数有的属性"""

    class C:
        pass

    obj = C()

    def func():
        pass

    return sorted(set(dir(func)) - set(dir(dir(obj))))


metro_data = [
    ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),  # <1>
    ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
    ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
    ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
    ('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
]


def example5_23() -> List[tuple]:
    """
    演示使用 itemgetter 排序一个元组列表
    根据元组的某个字段给元组列表排序
    """
    from operator import itemgetter

    # 如果把多个参数传给 itemgetter，它构建的函数会返回提取的值构成的元组：
    cc_name = itemgetter(1, 0)
    print([cc_name(item) for item in metro_data])
    return sorted(metro_data, key=itemgetter(2))  # <==> sorted(metro_areas, key=lambda data: data[2])


def example5_24() -> None:
    """
    定义一个 namedtuple，名为 metro_data，演示使用 attrgetter 处理它
    attrgetter 与 itemgetter 作用类似，它创建的函数根据名称提取对象的属性。如果把
    多个属性名传给 attrgetter，它也会返回提取的值构成的元组。此外，如果参数名中包
    含 .（点号），attrgetter 会深入嵌套对象，获取指定的属性。
    """
    from collections import namedtuple
    from operator import attrgetter
    LatLong = namedtuple('LatLong', 'lat long')  # 使用 namedtuple 定义 LatLong
    Metropolis = namedtuple('Metropolis', 'name cc pop coord')  # 再定义 Metropolis
    metro_areas = [Metropolis(name, cc, pop, LatLong(lat, long))
                   for name, cc, pop, (lat, long) in metro_data]

    print(metro_areas[0])
    print(metro_areas[0].coord.lat)

    name_lat = attrgetter('name', 'coord.lat')
    print([name_lat(city) for city in sorted(metro_areas, key=attrgetter('coord.lat'))])


def example5_25() -> None:
    """
    它的作用与 attrgetter 和 itemgetter 类似，它会自行创建函数。methodcaller 创建的函数会在对象上调用参数指定的方法
    """
    from operator import methodcaller
    s = 'The time has come'
    upcase = methodcaller('upper')
    print(upcase(s))
    print(s)
    print(s.upper())
    print(str.upper(s))

    hiphenate = methodcaller('replace', ' ', '-')
    print(hiphenate(s))
    print(s)
    print(s.replace(' ', '-'))


def example5_26() -> None:
    """
    使用functools.partial冻结参数
    functools.partial 这个高阶函数用于部分应用一个函数。部分应用是指，基于一个函数创
    建一个新的可调用对象，把原函数的某些参数固定。使用这个函数可以把接受一个或多个
    参数的函数改编成需要回调的 API，这样参数更少。
    """
    from operator import mul
    from functools import partial
    triple = partial(mul, 3)  # 使用 mul 创建 triple 函数，把第一个定位参数定为 3
    print(triple(7))
    print(list(map(triple, range(1, 10))))


if __name__ == '__main__':
    # print(example5_9())
    # print(example5_23())
    # example5_24()
    # example5_25()
    example5_26()
