from typing import Generator, Any


def example14_6() -> Generator[str, Any, None]:
    print('start')
    yield 'A'
    print('continue')
    yield 'B'
    print('End')


def main14_6() -> None:
    gen = example14_6()
    print('*' * 16)
    print(next(gen))
    print('*' * 16)
    print(next(gen))
    print('*' * 16)
    print(next(gen))


def example14_14() -> None:
    import itertools
    def vowel(c):
        return c.lower() in 'aeiou'

    print(list(filter(vowel, 'Aardvark')))
    print(list(itertools.filterfalse(vowel, 'Aardvark')))
    print(list(itertools.dropwhile(vowel, 'Aardvark')))
    print(list(itertools.takewhile(vowel, 'Aardvark')))
    print(list(itertools.compress('Aardvark', (1, 0, 1, 1, 0, 1))))
    print(list(itertools.islice('Aardvark', 4)))
    print(list(itertools.islice('Aardvark', 4, 7)))


if __name__ == '__main__':
    # main14_6()
    example14_14()
