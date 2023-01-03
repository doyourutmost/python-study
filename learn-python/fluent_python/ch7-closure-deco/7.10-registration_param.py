registry = set()  # <1> registry 现在是一个 set 对象，这样添加和删除函数的速度更快


def register(active=True):  # <2> register 接受一个可选的关键字参数
    def decorate(func):  # <3> decorate 这个内部函数是真正的装饰器；注意，它的参数是一个函数。
        print('running register(active=%s)->decorate(%s)'
              % (active, func))
        if active:  # <4> 只有 active 参数的值（从闭包中获取）是 True 时才注册 func
            registry.add(func)
        else:
            registry.discard(func)  # <5> 如果 active 不为真，而且 func 在 registry 中，那么把它删除
        return func  # <6> decorate 是装饰器，必须返回一个函数
    return decorate  # <7> register 是装饰器工厂函数，因此返回 decorate


@register(active=False)  # <8> @register 工厂函数必须作为函数调用，并且传入所需的参数
def f1():
    print('running f1()')


@register()  # <9> 即使不传入参数，register 也必须作为函数调用（@register()），即要返回真正的装饰器 decorate
def f2():
    print('running f2()')


def f3():
    print('running f3()')
