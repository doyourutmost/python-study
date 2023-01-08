import math
from array import array


class Vector2d:
    typecode = 'd'  # <1> typecode 是类属性，在 Vector2d 实例和字节序列之间转换时使用。

    def __init__(self, x, y):
        self.x = float(x)  # <2> 在 __init__ 方法中把 x 和 y 转换成浮点数，尽早捕获错误，以防调用 Vector2d 函数时传入不当参数。
        self.y = float(y)

    def __iter__(self):
        return (i for i in (self.x, self.y))  # <3> 定义 __iter__ 方法，把 Vector2d 实例变成可迭代的对象，这样才能拆包

    def __repr__(self):
        class_name = type(self).__name__
        return '{}({!r}, {!r})'.format(class_name, *self)  # <4> __repr__ 方法使用 {!r} 获取各个分量的表示形式，然后插值，构成一个字符串；
        # 因为Vector2d 实例是可迭代的对象，所以 *self 会把 x 和 y 分量提供给 format 函数

    def __str__(self):
        return str(tuple(self))  # <5> 从可迭代的 Vector2d 实例中可以轻松地得到一个元组，显示为一个有序对。

    def __bytes__(self):
        return (bytes([ord(self.typecode)]) +  # <6> 为了生成字节序列，我们把 typecode 转换成字节序列
                bytes(array(self.typecode, self)))  # <7> 迭代 Vector2d 实例，得到一个数组，再把数组转换成字节序列

    def __eq__(self, other):
        return tuple(self) == tuple(other)  # <8> 为了快速比较所有分量，在操作数中构建元组。对 Vector2d 实例来说，可以这样做，不过仍有问题。参见下面的警告
        # 在两个操作数都是 Vector2d 实例时可用，不过
        # 拿 Vector2d 实例与其他具有相同数值的可迭代对象相比，结果也是 True
        # （如 Vector(3, 4) == [3, 4]）。这个行为可以视作特性，也可以视作缺陷。

    def __abs__(self):
        return math.hypot(self.x, self.y)  # <9> 模是 x 和 y 分量构成的直角三角形的斜边长

    def __bool__(self):
        return bool(abs(self))  # <10> __bool__ 方法使用 abs(self) 计算模，然后把结果转换成布尔值，因此，0.0 是 False，非零值是 True


if __name__ == '__main__':
    v1 = Vector2d(3, 4)
    print('v1.x, v1.y:', v1.x, v1.y)  # 3.0 4.0
    x, y = v1  # 依赖 __iter__
    print('x, y = v1:', x, y)
    print('Vector2d(3, 4):', v1)

    v1_clone = eval(repr(v1))  # 这里使用 eval 函数克隆对象是为了说明 repr 方法。使用 copy.copy 函数克隆实例更安全也更快速
    print('repr(v1):', repr(v1))
    print('str(v1):', str(v1))
    print('v1 == v1_clone:', v1 == v1_clone)

    print('bytes(v1):', bytes(v1))  # bytes 函数会调用 __bytes__ 方法，生成实例的二进制表示形式
