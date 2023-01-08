import math
from array import array


class Vector2d:
    typecode = 'd'

    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

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
    # 内置的 format() 函数和 str.format() 方法把各个类型的格式化方式委托给相应的
    # .__format__(format_spec) 方法。format_spec 是格式说明符，它是：
    # (1) format(my_obj, format_spec) 的第二个参数，或者
    # (2) str.format() 方法的格式字符串，{} 里代换字段中冒号后面的部分
    brl = 1 / 2.43
    print('brl:', brl)
    print("format(brl, '0.4f'):", format(brl))
    print("(format(brl, '0.4f')):", format(brl, '0.4f'))

    # datetime 模块中的类，它们的 __format__ 方法使用的格式代码与 strftime() 函数一样。
    from datetime import datetime
    from time import strftime

    now = datetime.now()
    print("format(datetime.now(), '%H:%M:%S'), '%H:%M:%S'):", format(now, '%H:%M:%S'))
    print("strftime('%H:%M:%S'):", strftime('%H:%M:%S'))

    v1 = Vector2d(3, 4)
    # 如果类没有定义 __format__ 方法，从 object 继承的方法会返回 str(my_object)。我们为Vector2d 类定义了 __str__ 方法，因此可以这样做
    print("Vector2d(3, 4):", format(v1))
    # 然而，如果传入格式说明符，object.__format__ 方法会抛出 TypeError：TypeError: non-empty format string passed to object.__format__
    print("format(v1, '.3f'):", format(v1, '.3f'))
    print("format(v1, '.3e'):", format(v1, '.3e'))

    print("format(v1, '.3ep'):", format(v1, '.3ep'))
    print("format(v1, '0.5fp'):", format(v1, '0.5fp'))

