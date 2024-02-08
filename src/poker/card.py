from enum import Enum
from functools import total_ordering
from typing import Self


class Suit(Enum):
    SPADES = "♠"
    HEARTS = "♥"
    DIAMONDS = "♦"
    CLUBS = "♣"

    def __str__(self) -> str:
        return f"{self.value}"

    def __lt__(self, other):
        _sorted = list(Suit)
        return _sorted.index(self) > _sorted.index(other)


@total_ordering
class Rank(Enum):
    ACE = "A"
    KING = "K"
    QUEEN = "Q"
    JACK = "J"
    TEN = "10"
    NINE = "9"
    EIGHT = "8"
    SEVEN = "7"
    SIX = "6"
    FIVE = "5"
    FOUR = "4"
    THREE = "3"
    TWO = "2"

    def __str__(self) -> str:
        return f"{self.value}"

    def __lt__(self, other):
        _sorted = list(Rank)
        return _sorted.index(self) > _sorted.index(other)


class Joker(Enum):
    RED = "RedJoker"
    BLACK = "BlackJoker"

    def __str__(self) -> str:
        return f"{self.value}"

    def __lt__(self, __value: str) -> bool:
        _sorted = ["RedJoker", "BlackJoker"]
        return _sorted.index(self) > _sorted.index(__value)


class PlayingCard:
    rank: Rank
    suit: Suit

    def __init__(self, rank: Rank, suit: Suit) -> None:
        self.rank = rank
        self.suit = suit

    def __str__(self) -> str:
        return f"{self.suit}{self.rank}"

    def __lt__(self, other: Self):
        return (self.rank, self.suit) < (other.rank, other.suit)


if __name__ == "__main__":
    print(sorted(list(Rank)))
    print(sorted([1, 2, 3]))
    print(Rank.KING > Rank.ACE)
    print(Rank.ACE > Rank.KING)
    print(Rank.ACE == Rank.ACE)

    print(PlayingCard(Rank.ACE, Suit.HEARTS) > PlayingCard(Rank.KING, Suit.HEARTS))
