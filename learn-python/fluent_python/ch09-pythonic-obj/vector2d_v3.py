import math
from array import array


class Vector2d:
    typecode = 'd'

    def __init__(self, x, y):
        self.__x = float(x)  # 使用两个前导下划线（尾部没有下划线，或者有一个下划线），把属性标记为私有的。
        self.__y = float(y)

    @property  # @property 装饰器把读值方法标记为特性
    def x(self):  # 读值方法与公开属性同名，都是 x
        return self.__x

    @property
    def y(self):
        return self.__y

    def __iter__(self):
        return (i for i in (self.x, self.y))

    def __repr__(self):
        class_name = type(self).__name__
        return '{}({!r}, {!r})'.format(class_name, *self)

    def __str__(self):
        return str(tuple(self))

    def __bytes__(self):
        return (bytes([ord(self.typecode)]) +
                bytes(array(self.typecode, self)))

    def __eq__(self, other):
        return tuple(self) == tuple(other)

    def __hash__(self):
        return hash(self.x) ^ hash(self.y)

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    def angle(self):
        return math.atan2(self.y, self.x)

    def __format__(self, fmt_spec=''):
        if fmt_spec.endswith('p'):
            fmt_spec = fmt_spec[:-1]
            coords = (abs(self), self.angle())
            outer_fmt = '<{}, {}>'
        else:
            coords = self
            outer_fmt = '({}, {})'
        components = (format(c, fmt_spec) for c in coords)
        return outer_fmt.format(*components)

    @classmethod
    def frombytes(cls, octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(*memv)


if __name__ == '__main__':
    # 按照定义，目前 Vector2d 实例是不可散列的，因此不能放入集合（set）中：
    v1 = Vector2d(3, 4)
    v2 = Vector2d(3.1, 4.2)
    print(hash(v1))
    print(hash(v2))
    print({v1})
    # 为了把 Vector2d 实例变成可散列的，必须使用 __hash__ 方法（还需要 __eq__ 方法，前面 已经实现了）。此外，还要让向量不可变
    # 所以我们要把 x 和 y 分量设为只读特性
    # v1.x = 3.3 # AttributeError: can't set attribute

    # (两个前导下划线，尾部没有或最多有一个下划线）命名实例属性，Python 会把属性名存入实例的 __dict__ 属性中，而且会在前面加上一个下划线和类名
    print(v1.__dict__)


    class ShortVector2d(Vector2d):
        typecode = 'f'


    sv = ShortVector2d(1 / 11, 1 / 27)
    print('ShortVector2d(1/11, 1/27):', sv)
    print(' len(bytes(sv)):', len(bytes(sv)))  # 确认得到的字节序列长度为 9 字节，而不是之前的 17 字节

    pass
