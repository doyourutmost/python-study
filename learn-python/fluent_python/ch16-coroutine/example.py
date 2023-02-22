"""
协程可以身处四个状态中的一个。当前状态可以使用 inspect.getgeneratorstate(...) 函数确定，该函数会返回下述字符串中的一个。
'GEN_CREATED': 等待开始执行
'GEN_RUNNING': 解释器正在执行
'GEN_SUSPENDED': 在 yield 表达式处暂停
'GEN_CLOSED': 执行结束
"""
from functools import wraps
from inspect import getgeneratorstate


def averager():
    total = 0.0
    count = 0
    average = None
    while True:  # <1> 这个无限循环表明，只要调用方不断把值发给这个协程，它就会一直接收值，然后生成结果。仅当调用方在协程上调用 .close()
        # 方法，或者没有对协程的引用而被垃圾回收程序回收时，这个协程才会终止
        term = yield average  # <2> # 这里的 yield 表达式用于暂停执行协程，把结果发给调用方；还用于接收调用方后面发给协程的值，恢复无限循环
        total += term
        count += 1
        average = total / count


def coroutine(func):
    """装饰器：向前执行到第一个`yield`表达式，预激`func`"""

    @wraps(func)
    def primer(*args, **kwargs):  # <1> 把被装饰的生成器函数替换成这里的 primer 函数；调用 primer 函数时，返回预激后的生成器
        gen = func(*args, **kwargs)  # <2> 调用被装饰的函数，获取生成器对象
        next(gen)  # <3> 预激生成器
        return gen  # <4> 返回生成器

    return primer


def example16_1() -> None:
    def simple_coroutine():  # 协程使用生成器函数定义：定义体中有 yield 关键字
        print('-> coroutine started')
        x = yield  # yield 在表达式中使用；如果协程只需从客户那里接收数据，那么产出的值是 None——这个值是隐式指定的，因为 yield 关键字右边没有表达式
        print('-> coroutine received:', x)
        # 这里，控制权流动到协程定义体的末尾，导致生成器像往常一样抛出 StopIteration 异常

    my_cro = simple_coroutine()  # 与创建生成器的方式一样，调用函数得到生成器对象
    print("simple_coroutine():", my_cro)
    # next(my_cro)  # 首先要调用 next(...) 函数，因为生成器还没启动，没在 yield 语句处暂停，所以一开始无法发送数据
    # my_cro.send(None) # 同上，效果一样
    my_cro.send(42)  # 调用这个方法后，协程定义体中的 yield 表达式会计算出 42；现在，协程会恢复，一直运行到下一个 yield 表达式，或者终止


def example16_2() -> None:
    """产出两个值的协程"""

    def simple_coro2(a):
        print('-> Started: a =', a)
        b = yield a
        print('-> Received: b =', b)
        c = yield a + b
        print('-> Received: c =', c)

    my_coro2 = simple_coro2(14)
    from inspect import getgeneratorstate
    print("getgeneratorstate(my_coro2):",
          getgeneratorstate(my_coro2))  # inspect.getgeneratorstate 函数指明，处于 GEN_CREATED 状态（即协程未启动）
    print(next(my_coro2))
    print("getgeneratorstate(my_coro2):",
          getgeneratorstate(my_coro2))  # getgeneratorstate 函数指明，处于 GEN_SUSPENDED 状态（即协程在 yield 表达式处暂停）
    print(my_coro2.send(28))
    try:
        print(my_coro2.send(
            99))  # 把数字 99 发给暂停的协程；计算 yield 表达式，得到 99，然后把那个数绑定给 c。打印-> Received: c = 99 消息，然后协程终止，导致生成器对象抛出
        # StopIteration 异常。
    except StopIteration:
        pass

    print("getgeneratorstate(my_coro2):",
          getgeneratorstate(my_coro2))  # getgeneratorstate 函数指明，处于 GEN_CLOSED 状态（即协程执行结束）


def example16_3() -> None:
    coro_avg = averager()
    print(coro_avg)
    print(coro_avg.send(None))
    print(coro_avg.send(10))
    print(coro_avg.send(30))
    print(coro_avg.send(5))
    print(coro_avg.close())


def example16_5() -> None:
    """
    预激协程的装饰器
    如果不预激，那么协程没什么用。调用 my_coro.send(x) 之前，记住一定要调用 next(my_coro)
    """
    coro_avg = coroutine(averager)()
    print(coro_avg)
    print(coro_avg.send(10))
    print(coro_avg.send(30))
    print(coro_avg.send(5))
    print(coro_avg.close())


def example16_7() -> None:
    """
    终止协程和异常处理
    协程中未处理的异常会向上冒泡，传给 next 函数或 send 方法的调用方（即触发协程的对象）
    """
    coro_avg = coroutine(averager)()  # 使用 @coroutine 装饰器装饰的 averager 协程，可以立即开始发送值
    print(coro_avg.send(40))
    print(coro_avg.send(50))
    try:
        print(coro_avg.send('spam'))  # 发送的值不是数字，导致协程内部有异常抛出
    except TypeError as e:
        print(*e.args)
    print(coro_avg.send(60))  # 由于在协程内没有处理异常，协程会终止。如果试图重新激活协程，会抛出StopIteration异常


class DemoException(Exception):
    pass


def example16_8() -> None:
    """学习在协程中处理异常的测试代码"""

    def demo_exc_handling():
        print('-> coroutine started')
        while True:
            try:
                x = yield
            except DemoException:  # <1> 特别处理 DemoException 异常
                print('*** DemoException handled. Continuing...')
            else:  # <2> 如果没有异常，那么显示接收到的值
                print('-> coroutine received: {!r}'.format(x))
        raise RuntimeError('This line should never run.')  # <3> 这一行永远不会执

    exc_coro = demo_exc_handling()
    next(exc_coro)
    exc_coro.send(11)
    exc_coro.send(22)
    # exc_coro.close()
    # 把 DemoException 异常传入 demo_exc_handling 不会导致协程中止
    exc_coro.throw(DemoException)
    print(getgeneratorstate(exc_coro))
    # 如果无法处理传入的异常，协程会终止
    exc_coro.throw(ZeroDivisionError)


def example16_12() -> None:
    """使用 try/finally 块在协程终止时执行操作"""

    def demo_exc_handling():
        print('-> coroutine started')
        try:
            while True:
                try:
                    x = yield
                except DemoException:  # <1> 特别处理 DemoException 异常
                    print('*** DemoException handled. Continuing...')
                else:  # <2> 如果没有异常，那么显示接收到的值
                    print('-> coroutine received: {!r}'.format(x))
        finally:
            print('-> coroutine ending')

    exc_coro = demo_exc_handling()
    next(exc_coro)
    exc_coro.send(11)
    exc_coro.send(22)
    # exc_coro.close()
    # 把 DemoException 异常传入 demo_exc_handling 不会导致协程中止
    exc_coro.throw(DemoException)
    print(getgeneratorstate(exc_coro))
    # 如果无法处理传入的异常，协程会终止
    exc_coro.throw(ZeroDivisionError)


def example16_13() -> None:
    """为了说明如何返回值，每次激活协程时不会产出移动平均值。
    这么做是为了强调某些协程不会产出值，而是在最后返回一个值（通常是某种累计值）
    """
    from collections import namedtuple

    Result = namedtuple('Result', 'count average')

    def averager():
        total = 0.0
        count = 0
        average = None
        while True:
            term = yield
            if term is None:
                break  # <1> 为了返回值，协程必须正常终止；因此，这一版 averager 中有个条件判断，以便退出累计循环
            total += term
            count += 1
            average = total / count
        return Result(count, average)  # 返回一个 namedtuple，包含 count 和 average 两个字段。在 Python 3.3 之前，如果生成器返回值，解释器会报句法错误
        # return 表达式的值会偷偷传给调用方，赋值给 StopIteration 异常的一个属性。这样
        # 做有点不合常理，但是能保留生成器对象的常规行为——耗尽时抛出 StopIteration 异常

    coro_avg = averager()
    next(coro_avg)
    print(coro_avg.send(10))
    coro_avg.send(30)
    coro_avg.send(6.5)
    try:
        print(coro_avg.send(None))  # <2> 发送 None 会终止循环，导致协程结束，返回结果。一如既往，生成器对象会抛出StopIteration 异常。异常对象的 value 属性保存着返回的值
    except StopIteration as exc:
        print(*exc.args)


if __name__ == '__main__':
    # example16_1()
    example16_2()
    # example16_3()
    # example16_5()
    # example16_7()
    # example16_8()
    # example16_12()
    # example16_13()
