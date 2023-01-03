def factorial(n):
    """returns n!"""
    return 1 if n < 2 else n * factorial(n - 1)


if __name__ == '__main__':
    # 　创建并测试一个函数，然后读取它的 __doc__ 属性，再检查它的类型
    print(factorial(42))
    print(factorial.__doc__)
    print(type(factorial))

    # 　通过别的名称使用函数，再把函数作为参数传递
    fact = factorial
    print(fact)
    print(list(map(factorial, range(11))))

    # map、filter和reduce的现代替代品
    # 计算阶乘列表：map 和 filter 与列表推导比较
    print(list(map(factorial, filter(lambda n: n % 2, range(6)))))
    print([factorial(n) for n in range(6) if n % 2])

    # 使用 reduce 和 sum 计算 0~99 之和
    from functools import reduce
    from operator import add

    print(reduce(add, range(100)))
    print(sum(range(100)))

    # 使用 dir 函数可以探知 factorial 具有下述属性
    print(dir(factorial))
