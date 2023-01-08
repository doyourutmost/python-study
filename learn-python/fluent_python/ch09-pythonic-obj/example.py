from fluent_python.util.base_util import println


@println
def example9_4():
    class Demo:
        @classmethod
        def klassmeth(*args):
            return args  # 第一个参数始终是 Demo 类。

        @staticmethod
        def statmeth(*args):
            return args

    return "Demo.klassmeth('klassmeth'): {}\nDemo.statmeth('statmeth'): {}".format(Demo.klassmeth('klassmeth'),
                                                                                   Demo.statmeth('statmeth'))


if __name__ == '__main__':
    ''.format()
    example9_4()
