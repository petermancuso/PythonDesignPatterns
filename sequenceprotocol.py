import collections
from random import choice
from random import shuffle

Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    # First of two methods needed for immutable protocol
    def __len__(self):
        return len(self._cards)

    # Second of two methods needed for immutable protocol
    def __getitem__(self, item):
        return self._cards[item]

    # Third method needed to convert immutable protocol to mutable protocol
    def __setitem__(self, key, value):
        self._cards[key] = value


suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)

# Comment
def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]


deck = FrenchDeck()

for card in deck:
    print(card)

for card in sorted(deck, key=spades_high):
    print(card)


print(choice(deck))

shuffle(deck)

for card in deck:
    print(card)


