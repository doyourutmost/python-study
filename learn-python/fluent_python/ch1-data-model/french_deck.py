import collections

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


def spades_high(card):
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
    print(deck[0])
    print(len(deck))
    print(list(deck))

    # 迭代通常是隐式的，譬如说一个集合类型没有实现 __contains__ 方法，那么 in 运算符就会按顺序做一次迭代搜索
    print(Card('Q', 'hearts') in deck)

    sortDeck = sorted(deck, key=spades_high, reverse=True)
    print(list(sortDeck))
