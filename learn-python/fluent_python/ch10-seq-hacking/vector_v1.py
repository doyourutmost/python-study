
import math
import reprlib
from array import array


class Vector:
    typecode = 'd'

    def __init__(self, components):
        self._components = array(self.typecode, components)  # <1> self._components 是“受保护的”实例属性，把 Vector 的分量保存在一个数组中

    def __iter__(self):
        return iter(self._components)  # <2> 为了迭代，我们使用 self._components 构建一个迭代器

    def __repr__(self):
        components = reprlib.repr(self._components)  # <3> 使用 reprlib.repr() 函数获取 self._components 的有限长度表示形式
        # 这个函数用于生成大型结构或递归结构的安全表示形式，它会限制输出字符串的长度，用 '...' 表示截断的部分

        print(components)  # array('d', [0.0, 1.0, 2.0, 3.0, 4.0, ...])
        # （如 array('d',[0.0, 1.0, 2.0, 3.0, 4.0, ...])）
        components = components[components.find('['):-1]  # <4> 把字符串插入 Vector 的构造方法调用之前，去掉前面的 array('d' 和后面的 )
        return 'Vector({})'.format(components)

    def __str__(self):
        return str(tuple(self))

    def __bytes__(self):
        return (bytes([ord(self.typecode)]) +
                bytes(self._components))  # <5> 直接使用 self._components 构建 bytes 对象

    def __eq__(self, other):
        return tuple(self) == tuple(other)

    def __abs__(self):
        return math.sqrt(sum(x * x for x in self))  # <6> 不能使用 hypot 方法了，因此我们先计算各分量的平方之和，然后再使用 sqrt 方法开平方。

    def __bool__(self):
        return bool(abs(self))

    @classmethod
    def frombytes(cls, octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(memv)  # <7> 我们只需在 Vector2d.frombytes 方法的基础上改动最后一行：直接把 memoryview 传给构造方法，不用像前面那样使用 * 拆包


if __name__ == '__main__':
    v1 = Vector([3.1, 4.2])
    print('Vector([3.1, 4.2]):', v1)
    print('Vector((3, 4, 5)):', Vector((3, 4, 5)))
    print('Vector(range(10)):', Vector(range(10)))
    print('Vector(range(10)):', repr(Vector(range(10))))
