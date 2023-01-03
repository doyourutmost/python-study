class FooBar:
    def __init__(self, x=22):
        self.x = x


print(FooBar().x)


class Fibs:
    def __init__(self):
        self.a = 0
        self.b = 1

    def __next__(self):
        if self.a > 10000:
            raise StopIteration
        self.a, self.b = self.b, self.a + self.b
        return self.a

    def __iter__(self):
        return self


fibs = Fibs()
for f in fibs:
    if f > 1000:
        print(f)
        break
print(list(fibs))


def flatten(nested):
    try:
        # # 不迭代类似于字符串的对象：
        # try:
        #     nested + ''
        # except TypeError:
        #     pass
        # else:
        #     raise TypeError
        if isinstance(nested, str):
            raise TypeError
        for sublist in nested:
            for element in flatten(sublist):
                yield element
    except TypeError:
        yield nested


print(list(flatten([[[1], 2], 3, 4, [5, [6, 7]], 8])))
print(list(flatten(['foo', ['bar', ['baz']]])))

open("ss")
