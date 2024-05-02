# clockdeco_param.py

"""
>>> snooze(.1)  # doctest: +ELLIPSIS
[0.101...s] snooze(0.1) -> None
>>> clock('{name}: {elapsed}')(time.sleep)(.2)  # doctest: +ELLIPSIS
sleep: 0.20...
>>> clock('{name}({args}) dt={elapsed:0.3f}s')(time.sleep)(.2)
sleep(0.2) dt=0.201s
"""

# BEGIN CLOCKDECO_PARAM
import time

DEFAULT_FMT = '[{elapsed:0.8f}s] {name}({args}) -> {result}'


def clock(fmt=DEFAULT_FMT):  # <1> clock 是参数化装饰器工厂函数
    def decorate(func):  # <2> decorate 是真正的装饰器
        def clocked(*_args):  # <3>  clocked 包装被装饰的函数
            t0 = time.time()
            _result = func(*_args)  # <4> _result 是被装饰的函数返回的真正结果
            elapsed = time.time() - t0
            name = func.__name__
            args = ', '.join(repr(arg) for arg in _args)  # <5> _args 是 clocked 的参数，args 是用于显示的字符串
            result = repr(_result)  # <6> result 是 _result 的字符串表示形式，用于显示
            print(fmt.format(**locals()))  # <7> 这里使用 **locals() 是为了在 fmt 中引用 clocked 的局部变量
            return _result  # <8> clocked 会取代被装饰的函数，因此它应该返回被装饰的函数返回的值。

        return clocked  # <9> decorate 返回 clocked

    return decorate  # <10> clock 返回 decorate


if __name__ == '__main__':

    @clock()  # <11> 在这个模块中测试，不传入参数调用 clock()，因此应用的装饰器使用默认的格式 str。
    def snooze(seconds):
        time.sleep(seconds)


    for i in range(3):
        snooze(.123)

    snooze(.1)
    clock('{name}: {elapsed}')(time.sleep)(.2)
    clock('{name}({args}) dt={elapsed:0.3f}s')(time.sleep)(.2)
