import random

from tombola import Tombola


class BingoCage(Tombola):  # <1> # 明确指定 BingoCage 类扩展 Tombola 类

    def __init__(self, items):
        self._randomizer = random.SystemRandom()  # <2> # 假设我们将在线上游戏中使用这个
        self._items = []
        self.load(items)  # <3> # 委托 .load(...) 方法实现初始加载

    def load(self, items):
        self._items.extend(items)
        self._randomizer.shuffle(self._items)  # <4> 没有使用 random.shuffle() 函数，而是使用 SystemRandom 实例的 .shuffle() 方法

    def pick(self):  # <5>
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('pick from empty BingoCage')

    def __call__(self):  # <7>
        self.pick()
