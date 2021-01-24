'''
Deck of Cards

Piero Orderique
24 Jan 2021

design data structure for generic deck of cards
How would you subclass the data structures to implement blackjack?
'''
from random import randint

ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
values = {
    "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, 
    "9":9, "10":10, "J":11, "Q":12, "K":13, "A":14
}
suits = ["H", "D", "S", "C"]

class Card:
    def __init__(self, rank, suit) -> None:
        self.rank = rank
        self.suit = suit
        self.value = values[rank]
    
    def __str__(self) -> str:
        return self.rank + self.suit

class Deck:
    def __init__(self, *cards) -> None:
        self.deck = []
        if cards:
            for card in cards:
                self.deck.append(card)
        else:
            # create a full deck
            for suit in suits:
                for rank in ranks:
                    self.deck.append(Card(rank, suit))

    def shuffle(self):
        temp = []
        cards_left = len(self.deck)
        while cards_left:
            temp.append(self.deck.pop(randint(0, cards_left - 1)))
            cards_left -= 1
        self.deck = temp[:]
        del temp

    def is_empty(self):
        return bool(self.deck)

    def __add__(self, other):
        return Deck(*(self.deck + other.deck))

    def __str__(self) -> str:
        if not self.deck: 
            return "Empty Deck"
        res = ""
        for card in self.deck:
            res+= str(card) + " "
        return res
        
'''
To implement black jack, I would include another "Card Stack" class that would 
"pop" from the top each time a card was drawn. Addtionally, we could subclass
the deck class to represent a "hand" (ex class Hand(Deck)) and add methods to 
get the score and check if we have lost etc.
'''

deck = Deck(
    Card("A", "H"),
    Card("Q", "H"),
)
deck2 = Deck(
    Card("3", "S"),
    Card("5", "C"),
    Card("J", "D"),
)
