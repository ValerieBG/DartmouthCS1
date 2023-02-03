from card import *
from random import *

class Deck:
    def __init__(self):
        self.deck = [Card] * 52

    def add_standard_cards(self):
        for i in Card.suits:
            for j in Card.names:
                card = Card(Card.names[j], Card.suits[i])
                position = (i * len(Card.names)) + j
                self.deck[position] = card

    def shuffle(self):
        for i in self.deck:
            current_pos = i
            new_pos = randint(0, len(self.deck))
            temp = self.deck[current_pos]
            self.deck[new_pos] = temp

    def deal(self):
        return self.deck
