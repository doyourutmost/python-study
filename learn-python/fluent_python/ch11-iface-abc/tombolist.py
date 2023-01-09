from random import randrange

from tombola import Tombola


@Tombola.register  # <1> 把 Tombolist 注册为 Tombola 的虚拟子类
class TomboList(list):  # <2> Tombolist 扩展 list

    def pick(self):
        if self:  # <3> Tombolist 从 list 中继承 __bool__ 方法，列表不为空时返回 True。
            position = randrange(len(self))
            return self.pop(position)  # <4> ➍ pick 调用继承自 list 的 self.pop 方法，传入一个随机的元素索引
        else:
            raise LookupError('pop from empty TomboList')

    load = list.extend  # <5> Tombolist.load 与 list.extend 一样

    def loaded(self):
        return bool(self)  # <6> loaded 方法委托 bool 函数

    def inspect(self):
        return tuple(sorted(self))


if __name__ == '__main__':
    print("issubclass(TomboList, Tombola):", issubclass(TomboList, Tombola))
    t = TomboList(range(100))
    print("isinstance(t, Tombola):", isinstance(t, Tombola))
    print(TomboList.__mro__)  # 方法解析顺序
