class A:
    def ping(self):
        print('ping:', self)


class B(A):
    def pong(self):
        print('pong:', self)


class C(A):
    def pong(self):
        print('PONG:', self)


class D(B, C):

    def ping(self):
        super().ping()
        print('post-ping:', self)

    def pingpong(self):
        self.ping()
        super().ping()
        self.pong()
        super().pong()
        C.pong(self)


if __name__ == '__main__':
    d = D()
    d.pong()  # 直接调用 d.pong() 运行的是 B 类中的版本
    C.pong(d)  # 超类中的方法都可以直接调用，此时要把实例作为显式参数传入

    # Python 能区分 d.pong() 调用的是哪个方法，是因为 Python 会按照特定的顺序遍历继承图。这个顺序叫方法解析顺序
    print(D.mro())
    d.pingpong()
