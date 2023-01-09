import re
import reprlib

RE_WORD = re.compile(r'\w+')


class Sentence:

    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)

    def __iter__(self):
        for word in self.words:  # <1> 迭代 self.words
            yield word  # <2> 产出当前的 word
        return  # <3> 这个 return 语句不是必要的；这个函数可以直接“落空”，自动返回


if __name__ == '__main__':
    s = Sentence('"The time has come," the Walrus said,')
    print(s)

    for i in s:
        print(i)
