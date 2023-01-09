"""

Driving it with ``yield from``::

    >>> def summarize(results):
    ...     while True:
    ...         result = yield from averager()
    ...         results.append(result)
    ...
    >>> results = []
    >>> summary = summarize(results)
    >>> next(summary)
    >>> for height in data['girls;m']:
    ...     summary.send(height)
    ...
    >>> summary.send(None)
    >>> for height in data['boys;m']:
    ...     summary.send(height)
    ...
    >>> summary.send(None)
    >>> results == [
    ...     Result(count=10, average=1.4279999999999997),
    ...     Result(count=9, average=1.3888888888888888)
    ... ]
    True

"""

# BEGIN YIELD_FROM_AVERAGER
from collections import namedtuple

Result = namedtuple('Result', 'count average')


# the subgenerator
def averager():  # <1> 这里作为子生成器使用
    total = 0.0
    count = 0
    average = None
    while True:
        term = yield  # <2> main 函数中的客户代码发送的各个值绑定到这里的 term 变量上
        if term is None:  # <3> 至关重要的终止条件。如果不这么做，使用 yield from 调用这个协程的生成器会永远阻塞
            break
        total += term
        count += 1
        average = total / count
    return Result(count, average)  # <4> 返回的 Result 会成为 grouper 函数中 yield from 表达式的值


# the delegating generator
def grouper(results, key):  # <5> grouper 是委派生成器
    while True:  # <6> 这个循环每次迭代时会新建一个 averager 实例；每个实例都是作为协程使用的生成器对象。
        results[key] = yield from averager()  # <7>  grouper 发送的每个值都会经由 yield from 处理， 通过管道传给averager实例。
        # grouper 会在 yield from 表达式处暂停，等待 averager 实例处理客户端发来的值。averager 实例运行完毕后，返回的值绑定到 results[key] 上。while
        # 循环会不断创建averager 实例，处理更多的值


# the client code, a.k.a. the caller
def main(data):  # <8> main 函数是客户端代码，用 PEP 380 定义的术语来说，是“调用方”。这是驱动一切的函数
    results = {}
    for key, values in data.items():
        group = grouper(results,
                        key)  # <9> group 是调用 grouper 函数得到的生成器对象，传给 grouper
        # 函数的第一个参数是results，用于收集结果；第二个参数是某个键。group作为协程使用
        next(group)  # <10> 预激 group 协程
        for value in values:
            group.send(value)  # <11> 把各个 value 传给 grouper。传入的值最终到达 averager 函数中 term = yield 那一行；grouper 永远不知道传入的值是什么
        # group.send(
        #     None)  # important! <12>  None 传入 grouper，导致当前的 averager 实例终止，也让 grouper 继续运行，再创建一个 averager 实例，处理下一组值

    # print(results)  # uncomment to debug
    report(results)


# output report
def report(results):
    for key, result in sorted(results.items()):
        group, unit = key.split(';')
        print('{:2} {:5} averaging {:.2f}{}'.format(
            result.count, group, result.average, unit))


data = {
    'girls;kg':
        [40.9, 38.5, 44.3, 42.2, 45.2, 41.7, 44.5, 38.0, 40.6, 44.5],
    'girls;m':
        [1.6, 1.51, 1.4, 1.3, 1.41, 1.39, 1.33, 1.46, 1.45, 1.43],
    'boys;kg':
        [39.0, 40.8, 43.2, 40.8, 43.1, 38.6, 41.4, 40.6, 36.3],
    'boys;m':
        [1.38, 1.5, 1.32, 1.25, 1.37, 1.48, 1.25, 1.49, 1.46],
}

if __name__ == '__main__':
    main(data)

# END YIELD_FROM_AVERAGER
