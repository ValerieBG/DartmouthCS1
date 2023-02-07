# filename: card.py
# author:   Valerie Gadapati
# date:     Feb 12, 2023
# purpose:  to create a playing card with suits and values

class Card:
    suits = ["clubs", "diamonds", "spades", "hearts"]
    values = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]

    # initialize a card with a value and suit as given by the parameters
    def __init__(self, value, suit):
        self.value = Card.values[value - 1]
        self.suit = Card.suits[suit-1]

    # prints "value of suit" for a card object (e.g. 5 of clubs or Queen of hearts)
    def __str__(self):
        return self.value + " of " + self.suit
