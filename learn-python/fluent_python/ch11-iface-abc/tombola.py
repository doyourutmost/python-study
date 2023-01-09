import abc


class Tombola(abc.ABC):  # <1> 自己定义的抽象基类要继承 abc.ABC

    @abc.abstractmethod
    def load(self, iterable):  # <2> 抽象方法使用 @abstractmethod 装饰器标记，而且定义体中通常只有文档字符串
        """从可迭代对象中添加元素"""

    @abc.abstractmethod
    def pick(self):  # <3> 根据文档字符串，如果没有元素可选，应该抛出 LookupErro
        """随机删除元素，然后将其返回.

        如果实例为空，这个方法应该抛出`LookupError`.
        """

    def loaded(self):  # <4> 抽象基类可以包含具体方法
        """如果至少有一个元素，返回`True`，否则返回`False`."""
        return bool(self.inspect())  # <5> 抽象基类中的具体方法只能依赖抽象基类定义的接口（即只能使用抽象基类中的其他具体方法、抽象方法或特性）

    def inspect(self):
        """返回一个有序元组，由当前元素构成."""
        items = []
        while True:  # <6> 我们不知道具体子类如何存储元素，不过为了得到 inspect 的结果，我们可以不断调用 .pick() 方法，把 Tombola 清空
            try:
                items.append(self.pick())
            except LookupError:
                break
        self.load(items)  # <7> 然后再使用 .load(...) 把所有元素放回去
        return tuple(sorted(items))


if __name__ == '__main__':
    # 不符合 Tombola 要求的子类无法蒙混过关
    class Fake(Tombola):  # 把 Fake 声明为 Tombola 的子类
        def pick(self):
            return 13


    print(Fake)  # 创建了 Fake 类，目前没有错误
    f = Fake()  # 尝试实例化 Fake 时抛出了 TypeError
