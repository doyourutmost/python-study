"""
Sentence: access words by index
"""

import re
import reprlib

RE_WORD = re.compile(r'\w+')


class Sentence:

    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)  # <1> re.findall 函数返回一个字符串列表，里面的元素是正则表达式的全部非重叠匹配

    def __getitem__(self, index):
        return self.words[index]  # <2> self.words 中保存的是 .findall 函数返回的结果，因此直接返回指定索引位上的单词

    def __len__(self):  # <3> 为了完善序列协议，我们实现了 __len__ 方法；不过，为了让对象可以迭代，没必要实现这个方法
        return len(self.words)

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)  # <4> reprlib.repr 这个实用函数用于生成大型数据结构的简略字符串表示形式

    def __str__(self):
        return str(self.words)

    def __call__(self, *args, **kwargs):
        for w in self.words:
            print(w)


if __name__ == '__main__':
    s = Sentence('"The time has come," the Walrus said,')
    print(s)
    s()
    # for i in s:
    #     print(i)
    """
    序列可以迭代的原因：iter函数
    内置的 iter 函数有以下作用。
    (1) 检查对象是否实现了 __iter__ 方法，如果实现了就调用它，获取一个迭代器。
    (2) 如果没有实现 __iter__ 方法，但是实现了 __getitem__ 方法，Python 会创建一个迭代
    器，尝试按顺序（从索引 0 开始）获取元素。
    (3) 如果尝试失败，Python 抛出 TypeError 异常，通常会提示“C object is not iterable”（C
    对象不可迭代），其中 C 是目标对象所属的类。
    """