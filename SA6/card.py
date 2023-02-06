# filename: card.py
# author:   Valerie Gadapati
# date:     Feb 12, 2023
# purpose:  to create a playing cards with suits and values

class Card:
    suits = ["clubs", "diamonds", "spades", "hearts"]
    values = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]

    def __init__(self, value, suit):
        self.value = Card.values[value - 1]
        self.suit = Card.suits[suit-1]

    def __str__(self):
        return self.value + " of " + self.suit
