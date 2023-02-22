import collections
import random
import reprlib

# collections.namedtuple 用以构建只有少数属性但是没有方法的对象
Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck(object):
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

    def __repr__(self):
        return reprlib.repr(self._cards)


def spades_high(card: Card):
    """
    用点数来判定扑克牌的大小，2 最小、A 最大；
    同时还要加上对花色的判定，黑桃最大、红桃次之、方块再次、梅花最小
    :param card: 卡牌
    :return:
    """
    suit_values = dict(spades=3, hearts=2, diamonds=0, clubs=1)

    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]


if __name__ == '__main__':
    beer_card = Card('7', 'diamonds')
    print(beer_card)

    deck = FrenchDeck()
    print(deck[-1])  # <==> print(deck.__getitem__(0))

    print('len(deck): %s' % len(deck))
    print('list(deck): %s' % list(deck))

    print('随机抽取一张纸牌: %s' % (random.choice(deck),))
    print('随机抽取十张纸牌: %s' % random.choices(deck, k=10))

    print('只看牌面是 A 的牌:', deck[12::13])

    # 迭代通常是隐式的，譬如说一个集合类型没有实现 __contains__ 方法，那么 in 运算符就会按顺序做一次迭代搜索
    print("Card('Q', 'hearts') in deck:", Card('Q', 'hearts') in deck)

    print('排序:', list(sorted(deck, key=spades_high, reverse=True)))

    # 洗牌
    # random.shuffle(deck)  # 按照目前的设计，FrenchDeck 是不能洗牌的，因为这摞牌是不可变的（immutable）：卡牌和它们的位置都是固定的

    def set_card(self, position, card):
        """
        # 为 FrenchDeck 打猴子补丁，把它变成可变的，让 random.shuffle 函数能处理
        :param self:
        :param position:
        :param card:
        :return:
        """
        self._cards[position] = card


    FrenchDeck.__setitem__ = set_card
    random.shuffle(deck)
    print(deck)
