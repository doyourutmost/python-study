from math import hypot


class Vector(object):
    def __init__(self, x: int = 0, y: int = 0):
        self.x = x
        self.y = y

    # __repr__ 和 __str__ 的区别在于:
    # (1)后者是在 str() 函数被使用，或是在用 print 函数打印, 一个对象的时候才被调用的，并且它返回的字符串对终端用户更友好
    # (2)如果你只想实现这两个特殊方法中的一个，__repr__ 是更好的选择，因为如果一个对象没有 __str__ 函数，而 Python 又需要调用它的时候，解释器会用 __repr__ 作为替代
    # def __repr__(self):
    #     return 'Vector(%r, %r)' % (self.x, self.y)

    def __str__(self):
        return 'Vector({}, {})'.format(self.x, self.y)

    def __repr__(self):
        return 'Vector(%r, %r)' % (self.x, self.y)

    def __abs__(self):
        return hypot(self.x, self.y)

    # 默认情况下，我们自己定义的类的实例总被认为是真的，除非这个类对 __bool__ 或者 __
    # len__ 函数有自己的实现。bool(x) 的背后是调用 x.__bool__() 的结果；如果不存在 __
    # bool__ 方法，那么 bool(x) 会尝试调用 x.__len__()。若返回 0，则 bool 会返回 False；否
    # 则返回 True
    def __bool__(self):
        # return bool(abs(self))
        return bool(self.x or self.y)

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    def __int__(self):
        return self.x * self.x + self.y * self.y


if __name__ == '__main__':
    v1 = Vector(2, 4)
    v2 = Vector(2, 1)
    v3 = Vector(0, 0)
    print('v1 + v2', v1 + v2)

    print('abs(v1):', abs(v1))
    if v1:
        print("v1 is True")
    if not v3:
        print("v3 is False")

    print("Vector('1', '2'):", Vector('1', '2'))
    print("Vector('1', '2'):", '%r' % Vector('1', '2'))
    print("int(v1):", int(v1))

    t = (1, 2, [30, 40])
    t[2] += [50, 60]
    print(t)
