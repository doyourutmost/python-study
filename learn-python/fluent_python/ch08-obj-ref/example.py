def example8_5() -> None:
    """
   装饰器是可调用的对象，其参数是另一个函数（被装饰的函数）。 装饰器可能会处理被装
    饰的函数，然后把它返回，或者将其替换成另一个函数或可调用对象
    """
    # 元组的相对不可变性
    t1 = (1, 2, [30, 40])  # t1 不可变，但是 t1[-1] 可变
    t2 = (1, 2, [30, 40])  # 构建元组 t2，它的元素与 t1 一样
    print('t1 == t2: %s' % (t1 == t2))  # 虽然 t1 和 t2 是不同的对象，但是二者相等——与预期相符
    print('t1 is t2: %s' % (t1 is t2))

    print('id(t1[-1]): %s' % id(t1[-1]))
    t1[-1].append(99)  # 就地修改 t1[-1] 列表
    print('t1: %s' % repr(t1))
    print('id(t1[-1]): %s' % id(t1[-1]))  # t1[-1] 的标识没变，只是值变了

    print('t1 == t2: %s' % (t1 == t2))  # 现在，t1 和 t2 不相等


def example8_10() -> None:
    """
    循环引用：b 引用 a，然后追加到 a 中；deepcopy 会想办法复制 a
    """
    a = [10, 20]
    b = [a, 30]
    a.append(b)

    from copy import deepcopy
    c = deepcopy(a)
    print(c)


def example8_11() -> None:
    """
    函数可能会修改接收到的任何可变对象
    """

    def f(a, b):
        a += b
        return a

    x = 1
    y = 2
    print('f(x, y): %r ==>%r' % (f(x, y), x))

    a = [1, 2]
    b = [3, 4]
    print('f(a, b): %r ==>%r' % (f(a, b), a))

    t1 = (10, 20)
    t2 = (30, 40)
    print('f(t1, t2): %r ==>%r' % (f(t1, t2), t1))

    s1 = 'ab'
    s2 = 'cd'
    print('f(s1, s2): %r ==>%r' % (f(s1, s2), s1))


if __name__ == '__main__':
    # example8_5()
    # example8_10()
    example8_11()
