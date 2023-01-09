class ArithmeticProgression:

    def __init__(self, begin, step, end=None):  # __init__ 方法需要两个参数：begin 和 step。end 是可选的，如果值是 None，那么生成的是无穷数列
        self.begin = begin
        self.step = step
        self.end = end  # None -> "infinite" series

    def __iter__(self):
        result = type(self.begin + self.step)(self.begin)  # 这一行把 self.begin 赋值给 result，不过会先强制转换成前面的加法算式得到的类型
        forever = self.end is None  # 为了提高可读性，我们创建了 forever 变量，如果 self.end 属性的值是 None，那么forever 的值是 True，因此生成的是无穷数
        while forever or result < self.end:
            yield result  # 生成当前的 result 值。
            result += self.step


if __name__ == '__main__':
    ap = ArithmeticProgression(1, .5, 3)
    print(list(ap))
