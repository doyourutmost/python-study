import random

from tombola import Tombola


class LotteryBlower(Tombola):

    def __init__(self, iterable):
        self._balls = list(iterable)  # <1> # 初始化方法接受任何可迭代对象：把参数构建成列表

    def load(self, iterable):
        self._balls.extend(iterable)

    def pick(self):
        try:
            position = random.randrange(
                len(self._balls))  # <2> 如果范围为空，random.randrange(...) 函数抛出 ValueError，为了兼容 Tombola，我们捕获它，抛出 LookupError
        except ValueError:
            raise LookupError('pick from empty LotteryBlower')
        return self._balls.pop(position)  # <3> # 否则，从 self._balls 中取出随机选中的元素

    def loaded(self):  # <4>
        return bool(self._balls)  # 覆盖 loaded 方法，避免调用 inspect 方法

    def inspect(self):  # <5>
        return tuple(sorted(self._balls))  # 覆盖 inspect 方法
