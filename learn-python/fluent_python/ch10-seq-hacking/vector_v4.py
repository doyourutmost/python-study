import functools
import math
import numbers
import operator
import reprlib
from array import array


class Vector:
    typecode = 'd'

    def __init__(self, components):
        self._components = array(self.typecode, components)

    def __iter__(self):
        return iter(self._components)

    def __repr__(self):
        components = reprlib.repr(self._components)
        components = components[components.find('['):-1]
        return 'Vector({})'.format(components)

    def __str__(self):
        return str(tuple(self))

    def __bytes__(self):
        return (bytes([ord(self.typecode)]) +
                bytes(self._components))

    def __eq__(self, other):
        return (len(self) == len(other) and
                all(a == b for a, b in zip(self, other)))

    def __hash__(self):
        # print(self)  # 调用 str(self)
        hashes = (hash(x) for x in self)  # 创建一个生成器表达式，惰性计算各个分量的散列值
        return functools.reduce(operator.xor, hashes, 0)

    def __abs__(self):
        return math.sqrt(sum(x * x for x in self))

    def __bool__(self):
        return bool(abs(self))

    def __len__(self):
        return len(self._components)

    def __getitem__(self, index):
        cls = type(self)
        if isinstance(index, slice):
            return cls(self._components[index])
        elif isinstance(index, numbers.Integral):
            return self._components[index]
        else:
            msg = '{cls.__name__} indices must be integers'
            raise TypeError(msg.format(cls=cls))

    shortcut_names = 'xyzt'

    def __getattr__(self, name):
        cls = type(self)
        if len(name) == 1:
            pos = cls.shortcut_names.find(name)
            if 0 <= pos < len(self._components):
                return self._components[pos]
        msg = '{.__name__!r} object has no attribute {!r}'
        raise AttributeError(msg.format(cls, name))

    @classmethod
    def frombytes(cls, octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(memv)


if __name__ == '__main__':
    v1 = Vector([3, 4])
    v2 = Vector([3.1, 4.2])
    v3 = Vector([3, 4, 5])
    v6 = Vector(range(6))
    print("hash(v1), hash(v3), hash(v6):", hash(v1), hash(v3), hash(v6))

    # zip 内置函数的使用示例
    # zip 有个奇怪的特性：当一个可迭代对象耗尽后，它不发出警告就停止

    print("zip(range(3), 'ABC'):", zip(range(3), 'ABC'))
    print("list(zip(range(3), 'ABC'):", list(zip(range(3), 'ABC')))
    print("list(zip(range(3), 'ABC', [0.0, 1.1, 2.2, 3.3])):", list(zip(range(3), 'ABC', [0.0, 1.1, 2.2, 3.3])))
    from itertools import zip_longest
    # 使用可选的 fillvalue（默认值为
    # None）填充缺失的值，因此可以继续产出，直到最长的可迭代对象耗尽。
    print("list(zip_longest(range(3), 'ABC', [0.0, 1.1, 2.2, 3.3], fillvalue=-1)):",
          list(zip_longest(range(3), 'ABC', [0.0, 1.1, 2.2, 3.3], fillvalue=-1)))

    pass
