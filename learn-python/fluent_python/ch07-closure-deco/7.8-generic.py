"""
使用 @singledispatch 装饰的普通函数会变成
泛函数（generic function）：根据第一个参数的类型，以不同方式执行相同操作的一组函
数。
"""

import html
import numbers
from collections import abc
from functools import singledispatch


@singledispatch  # <1> @singledispatch 标记处理 object 类型的基函数
def htmlize(obj):
    content = html.escape(repr(obj))
    return '<pre>{}</pre>'.format(content)


@htmlize.register(str)  # <2> 各个专门函数使用 @«base_function».register(«type») 装饰。
def _(text):  # <3> 专门函数的名称无关紧要；_ 是个不错的选择，简单明了
    content = html.escape(text).replace('\n', '<br>\n')
    return '<p>{0}</p>'.format(content)


@htmlize.register(numbers.Integral)  # <4> 为每个需要特殊处理的类型注册一个函数。numbers.Integral 是 int 的虚拟超类
def _(n):
    return '<pre>{0} (0x{0:x})</pre>'.format(n)


@htmlize.register(tuple)  # <5> 可以叠放多个 register 装饰器，让同一个函数支持不同类型。
@htmlize.register(abc.MutableSequence)
def _(seq):
    inner = '</li>\n<li>'.join(htmlize(item) for item in seq)
    return '<ul>\n<li>' + inner + '</li>\n</ul>'


if __name__ == '__main__':
    print(htmlize({1, 2, 3}))  # <pre>{1, 2, 3}</pre>
    print(htmlize(abs))  # <pre>&lt;built-in function abs&gt;</pre>
    print(htmlize('Heimlich & Co.\n- a game'))
    """
    <p>Heimlich &amp; Co.<br>
    - a game</p>
    """
    print(htmlize(42))  # <pre>42 (0x2a)</pre>
    print(htmlize(['alpha', 66, {3, 2, 1}]))
    """
    <ul>
    <li><p>alpha</p></li>
    <li><pre>66 (0x42)</pre></li>
    <li><pre>{1, 2, 3}</pre></li>
    </ul>
    """
