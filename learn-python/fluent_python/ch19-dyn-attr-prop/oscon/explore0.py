"""
explore0.py: Script to explore the OSCON schedule feed

# BEGIN EXPLORE0_DEMO
    >>> from osconfeed import load
    >>> raw_feed = load()
    >>> feed = FrozenJSON(raw_feed)  # <1>
    >>> len(feed.Schedule.speakers)  # <2>
    357
    >>> sorted(feed.Schedule.keys())  # <3>
    ['conferences', 'events', 'speakers', 'venues']
    >>> for key, value in sorted(feed.Schedule.items()): # <4>
    ...     print('{:3} {}'.format(len(value), key))
    ...
      1 conferences
    484 events
    357 speakers
     53 venues
    >>> feed.Schedule.speakers[-1].name  # <5>
    'Carina C. Zona'
    >>> talk = feed.Schedule.events[40]
    >>> type(talk)  # <6>
    <class 'explore0.FrozenJSON'>
    >>> talk.name
    'There *Will* Be Bugs'
    >>> talk.speakers  # <7>
    [3471, 5199]
    >>> talk.flavor  # <8>
    Traceback (most recent call last):
      ...
    KeyError: 'flavor'

# END EXPLORE0_DEMO

"""

# BEGIN EXPLORE0
from collections import abc


class FrozenJSON:
    """A read-only façade for navigating a JSON-like object
       using attribute notation
    """

    def __init__(self, mapping):
        self.__data = dict(mapping)  # <1>

    def __getattr__(self, name):  # <2>
        if hasattr(self.__data, name):
            return getattr(self.__data, name)  # <3>
        else:
            return FrozenJSON.build(self.__data[name])  # <4>

    @classmethod
    def build(cls, obj):  # <5>
        if isinstance(obj, abc.Mapping):  # <6>
            return cls(obj)
        elif isinstance(obj, abc.MutableSequence):  # <7>
            return [cls.build(item) for item in obj]
        else:  # <8>
            return obj


# END EXPLORE0

if __name__ == '__main__':
    from osconfeed import load

    raw_feed = load()
    feed = FrozenJSON(raw_feed)  # 传入嵌套的字典和列表组成的 raw_feed，创建一个 FrozenJSON 实例
    print(len(feed.Schedule.speakers))  # FrozenJSON 实例能使用属性表示法遍历嵌套的字典；这里，我们获取演讲者列表的元素数量
    print(sorted(feed.Schedule.keys()))  # 也可以使用底层字典的方法，例如 .keys()，获取记录集合的名称
    for key, value in sorted(feed.Schedule.items()):  # 使用 items() 方法获取各个记录集合及其内容，然后显示各个记录集合中的元素数量
        print('{:3} {}'.format(len(value), key))
    print(feed.Schedule.speakers[-1].name)  # 列表，例如 feed.Schedule.speakers，仍是列表；但是，如果里面的元素是映射，会转换成 FrozenJSON 对象
    talk = feed.Schedule.events[40]
    print(talk)
    print(type(talk))
    print(talk.name)
    print(talk.speakers)
    print(talk.flavor)
    #
