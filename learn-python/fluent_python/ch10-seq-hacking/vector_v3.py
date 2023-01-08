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
        cls = type(self)  # <1> 获取 Vector，后面待用
        if len(name) == 1:  # <2>  如果属性名只有一个字母，可能是 shortcut_names 中的一个
            pos = cls.shortcut_names.find(name)  # <3> 查找那个字母的位置；str.find 还会定位 'yz'，但是我们不需要，因此在前一行做了测试
            if 0 <= pos < len(self._components):  # <4> 如果位置落在范围内，返回数组中对应的元素
                return self._components[pos]
        msg = '{.__name__!r} object has no attribute {!r}'  # <5> 如果测试都失败了，抛出 AttributeError，并指明标准的消息文本
        raise AttributeError(msg.format(cls, name))

    def __setattr__(self, name, value):
        cls = type(self)
        if len(name) == 1:  # <1> 特别处理名称是单个字符的属性
            if name in cls.shortcut_names:  # <2> 如果 name 是 xyzt 中的一个，设置特殊的错误消息
                error = 'readonly attribute {attr_name!r}'
            elif name.islower():  # <3> 如果 name 是小写字母，为所有小写字母设置一个错误消息
                error = "can't set attributes 'a' to 'z' in {cls_name!r}"
            else:
                error = ''  # <4> 否则，把错误消息设为空字符串
            if error:  # <5>
                msg = error.format(cls_name=cls.__name__, attr_name=name)
                raise AttributeError(msg)
        super().__setattr__(name, value)  # <6> 默认情况：在超类上调用 __setattr__ 方法，提供标准行为

    @classmethod
    def frombytes(cls, octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(memv)


if __name__ == '__main__':
    # 属性查找失败后，解释器会调用 __getattr__ 方法。简单来说，对 my_obj.x 表达式，Python
    # 会检查 my_obj 实例有没有名为 x 的属性；如果没有，到类（my_obj.__class__）中查找；如果
    # 还没有，顺着继承树继续查找。4 如果依旧找不到，调用 my_obj 所属类中定义的 __getattr__
    # 方法，传入 self 和属性名称的字符串形式（如 'x'）
    v1 = Vector(range(5))
    print("Vector(range(5)):", v1)
    print("v1.x:", v1.x)  # 使用 v.x 获取第一个元素（v[0]）
    # v1.x = 10  # 为 v.x 赋新值。这个操作应该抛出异常
    print("v1.x:", v1.x)  # 读取 v.x，得到的是新值，10
    print("v1:", v1)
    # print(" v1[0]:", v1[0])
    # v1[0] = 111
    # print("v1[0]:", v1[0])  # 读取 v.x，得到的是新值，10

    v1.w = 99
    v1.x = 88
