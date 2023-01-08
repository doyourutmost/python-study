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

    @classmethod  # <1> 类方法使用 classmethod 装饰器修饰。
    def frombytes(cls, octets):  # <2> 不用传入 self 参数；相反，要通过 cls 传入类本身。
        typecode = chr(octets[0])  # <3> 从第一个字节中读取 typecode。
        memv = memoryview(octets[1:]).cast(typecode)  # <4> 使用传入的 octets 字节序列创建一个 memoryview，然后使用 typecode 转换。
        return cls(*memv)  # <5> 拆包转换后的 memoryview，得到构造方法所需的一对参数


if __name__ == '__main__':
    v1 = Vector2d(3, 4)
    v1_clone = Vector2d.frombytes(bytes(v1))
    print('Vector2d.frombytes(bytes(v1)):', v1_clone)
    print('v1 == v1_clone:', v1 == v1_clone)
