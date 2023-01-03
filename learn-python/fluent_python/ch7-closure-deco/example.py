"""
装饰器的一大特性是，能把被装饰的函数替换成其他函数。
第二个特性是，装饰器在加载模块时立即执行
"""


def example7_1() -> None:
    """
   装饰器是可调用的对象，其参数是另一个函数（被装饰的函数）。 装饰器可能会处理被装
    饰的函数，然后把它返回，或者将其替换成另一个函数或可调用对象
    """

    # 装饰器通常把函数替换成另一个函数
    def deco(func):
        def inner():
            print('running inner()')

        return inner  # deco 返回 inner 函数对象

    @deco  # 使用 deco 装饰 target。
    def target():
        print('running target()')

    target()  # 调用被装饰的 target 其实会运行 inner
    print(target)  # 审查对象，发现 target 现在是 inner 的引用。


if __name__ == '__main__':
    example7_1()
