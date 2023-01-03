"""
装饰器的一个关键特性是，它们在被装饰的函数定义之后立即运行。这通常是在导入时（即 Python 加载模块时）
"""
registry = []  # <1> registry 保存被 @register 装饰的函数引用。


def register(func):  # <2> register 的参数是一个函数
    print('running register(%s)' % func)  # <3> 为了演示，显示被装饰的函数
    registry.append(func)  # <4> 把 func 存入 registry。
    return func  # <5> 返回 func：必须返回函数；这里返回的函数与通过参数传入的一样


@register  # <6> 返回 func：必须返回函数；这里返回的函数与通过参数传入的一样
def f1():
    print('running f1()')


@register
def f2():
    print('running f2()')


def f3():  # <7> f3 没有装饰
    print('running f3()')


def main():  # <8> main 显示 registry，然后调用 f1()、f2() 和 f3()。
    print('running main()')
    print('registry ->', registry)
    f1()
    f2()
    f3()


if __name__ == '__main__':
    main()
