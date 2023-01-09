"""




Tests of ``+`` with mixed types::

    >>> v1 + (10, 20, 30)
    Vector([13.0, 24.0, 35.0])
    >>> from vector2d_v3 import Vector2d
    >>> v2d = Vector2d(1, 2)
    >>> v1 + v2d
    Vector([4.0, 6.0, 5.0])


Tests of ``+`` with mixed types, swapped operands::

    >>> (10, 20, 30) + v1
    Vector([13.0, 24.0, 35.0])
    >>> from vector2d_v3 import Vector2d
    >>> v2d = Vector2d(1, 2)
    >>> v2d + v1
    Vector([4.0, 6.0, 5.0])


Tests of ``+`` with an unsuitable operand:

    >>> v1 + 1
    Traceback (most recent call last):
      ...
    TypeError: unsupported operand type(s) for +: 'Vector' and 'int'
    >>> v1 + 'ABC'
    Traceback (most recent call last):
      ...
    TypeError: unsupported operand type(s) for +: 'Vector' and 'str'
"""

import functools
import itertools
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
        hashes = (hash(x) for x in self)
        return functools.reduce(operator.xor, hashes, 0)

    # BEGIN VECTOR_V6_UNARY
    def __abs__(self):
        return math.sqrt(sum(x * x for x in self))

    def __neg__(self):
        return Vector(-x for x in self)  # <1> 为了计算 -v，构建一个新 Vector 实例，把 self 的每个分量都取反

    def __pos__(self):
        return Vector(self)  # <2> 为了计算 +v，构建一个新 Vector 实例，传入 self 的各个分量

    # END VECTOR_V6_UNARY

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
            msg = '{.__name__} indices must be integers'
            raise TypeError(msg.format(cls))

    shortcut_names = 'xyzt'

    def __getattr__(self, name):
        cls = type(self)
        if len(name) == 1:
            pos = cls.shortcut_names.find(name)
            if 0 <= pos < len(self._components):
                return self._components[pos]
        msg = '{.__name__!r} object has no attribute {!r}'
        raise AttributeError(msg.format(cls, name))

    def angle(self, n):
        r = math.sqrt(sum(x * x for x in self[n:]))
        a = math.atan2(r, self[n - 1])
        if (n == len(self) - 1) and (self[-1] < 0):
            return math.pi * 2 - a
        else:
            return a

    def angles(self):
        return (self.angle(n) for n in range(1, len(self)))

    def __format__(self, fmt_spec=''):
        if fmt_spec.endswith('h'):  # hyperspherical coordinates
            fmt_spec = fmt_spec[:-1]
            coords = itertools.chain([abs(self)],
                                     self.angles())
            outer_fmt = '<{}>'
        else:
            coords = self
            outer_fmt = '({})'
        components = (format(c, fmt_spec) for c in coords)
        return outer_fmt.format(', '.join(components))

    @classmethod
    def frombytes(cls, octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(memv)

    def __add__(self, other):
        try:
            # pairs 是个生成器，它会生成 (a, b) 形式的元组，其中 a 来自 self，b 来自 other。如
            # 果 self 和 other 的长度不同，使用 fillvalue 填充较短的那个可迭代对象
            pairs = itertools.zip_longest(self, other, fillvalue=0.0)
            return Vector(a + b for a, b in pairs)  # 构建一个新 Vector 实例，使用生成器表达式计算 pairs 中各个元素的和
        except TypeError:  # 如果中缀运算符方法抛出异常，就终止了运算符分派机制。对 TypeError 来说，通常最好将其捕获，然后返回 NotImplemented
            return NotImplemented

    def __radd__(self, other):
        return self + other  # __radd__ 直接委托 __add__。


if __name__ == '__main__':
    # abs、-、+
    v1 = Vector([3, 4])
    print("abs(Vector([3, 4])):", abs(v1))
    print("-Vector([3, 4]):", -v1)
    print("+Vector([3, 4]):", +v1)

    # +
    v1 = Vector([3, 4, 5])
    v2 = Vector([6, 7, 8])
    print("Vector([3, 4, 5])+Vector([6, 7, 8]):", Vector([3, 4, 5]) + Vector([6, 7, 8]))
    v3 = Vector([1, 2])
    print("Vector([1, 2])+Vector([6, 7, 8]):", Vector([1, 2]) + Vector([6, 7, 8]))

    print("[10, 20, 30]+Vector([6, 7, 8]):", [10, 20, 30] + Vector([6, 7, 8]))
    print("(1,)+Vector([6, 7, 8]):", (1,) + Vector([6, 7, 8]))

    # v1 + 3 # 如果左操作数是 Vector 之外的对象，第一版 Vector.__add__ 方法无法处理
    # 为了支持涉及不同类型的运算，Python 为中缀运算符特殊方法提供了特殊的分派机制。对
    # 表达式 a + b 来说，解释器会执行以下几步操作（见图 13-1）。
    # (1) 如果 a 有 __add__ 方法，而且返回值不是 NotImplemented，调用 a.__add__(b)，然后返回结果。
    # (2) 如果 a 没有 __add__ 方法，或者调用 __add__ 方法返回 NotImplemented，检查 b 有没有
    # __radd__ 方法，如果有，而且没有返回 NotImplemented，调用 b.__radd__(a)，然后返回结果。
    # (3) 如果 b 没有 __radd__ 方法，或者调用 __radd__ 方法返回 NotImplemented，抛出 TypeError，
    # 并在错误消息中指明操作数类型不支持。

    # v1 + 1
    # v1 + 'ABC'
    print([1, 2] == (1, 2))

