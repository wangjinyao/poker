import itertools
import random

from poker.card import PlayingCard, Rank, Suit


class Deck(object):
    """牌桌"""

    cards: list[PlayingCard]

    def __init__(self) -> None:
        """初始化牌桌"""
        self.cards = [PlayingCard(*i) for i in itertools.product(Rank, Suit)]

    def shuffle(self) -> None:
        """洗牌，返回有序牌组"""
        random.shuffle(self.cards)

    def sort(self, reverse=False) -> None:
        """排序"""
        self.cards.sort(reverse=reverse)
        # self.cards = sorted(self.cards, key=lambda c: (c.rank, c.suit), reverse=reverse)

    def deal(self):
        """发1张牌"""
        if self.cards:
            card = self.cards.pop(random.randrange(len(self.cards)))
            return card
        else:
            return None

    def __str__(self):
        card_str = [str(card) for card in self.cards]
        return ", ".join(card_str)

    def __len__(self):
        return len(self.cards)


if __name__ == "__main__":
    deck = Deck()
    print(deck)
    deck.shuffle()
    print(deck)

    card = deck.deal()
    print(card)
    print(deck)
