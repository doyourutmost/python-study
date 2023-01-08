import math
import numbers
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
        return tuple(self) == tuple(other)

    def __abs__(self):
        return math.sqrt(sum(x * x for x in self))

    def __bool__(self):
        return bool(abs(self))

    def __len__(self):
        return len(self._components)

    def __getitem__(self, index):
        cls = type(self)  # <1> 获取实例所属的类（即 Vector），供后面使用
        if isinstance(index, slice):  # <2> 如果 index 参数的值是 slice 对象
            print(index)  # slice(1, 4, None)
            return cls(self._components[index])  # <3> 调用类的构造方法，使用 _components 数组的切片构建一个新 Vector 实例
        elif isinstance(index, numbers.Integral):  # <4> 如果 index 是 int 或其他整数类型
            return self._components[index]  # <5>
        else:
            msg = '{cls.__name__} indices must be integers'
            raise TypeError(msg.format(cls=cls))  # <6>

    @classmethod
    def frombytes(cls, octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(memv)


if __name__ == '__main__':
    v1 = Vector([3, 4, 5])
    print('len(v1):', len(v1))
    print('v1[0], v1[-1]:', v1[0], v1[-1])

    v7 = Vector(range(7))
    print(repr(v7[1:4]))
    print(repr(v7[1, 4]))  # Vector 不支持多维索引，因此索引元组或多个切片会抛出错误

    # slice 是内置的类型
    print("slice:", slice)
    print("dir(slice):", dir(slice))


    class MySeq:
        def __getitem__(self, index):
            return index


    s = MySeq()
    print("s[1]:", s[1])
    print("s[1:4]:", s[1:4])
    print("s[1:4:2]:", s[1:4:2])
    print("s[1:4:2,9]:", s[1:4:2, 9])
    print("s[1:4:2,7:9]:", s[1:4:2, 7:9])

    #  S.indices(len) -> (start, stop, stride) 给定长度为 len 的序列，计算 S 表示的扩展切片的起始（start）和结尾（stop）索
    # 引，以及步幅（stride）。超出边界的索引会被截掉，这与常规切片的处理方式一样
    print("slice(None, 10, 2).indices(5):", slice(None, 10, 2).indices(5))  # 'ABCDE'[:10:2] 等同于 'ABCDE'[0:5:2]
    print("slice(-3, None, None).indices(5):", slice(-3, None, None).indices(5))  # ABCDE'[-3:] 等同于 'ABCDE'[2:5:1]
