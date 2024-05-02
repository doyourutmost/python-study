"""Python 3 引入了 nonlocal 声明。它的作用是把变量标记为自由变量，
即使在函数中为变量赋予新值了，也会变成自由变量。"""


def make_averager():
    """
    计算移动平均值，不保存所有历史
    :return: 平均值
    """
    count = 0
    total = 0

    def averager(new_value):
        nonlocal count, total

        count += 1
        total += new_value
        return total / count

    return averager


if __name__ == '__main__':
    averager = make_averager()
    print(averager(1))
    print(averager(2))
    print(averager(3))
    print(averager(4))
    print(averager(5))
    print(averager(6))
