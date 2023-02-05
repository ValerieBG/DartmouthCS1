# filename: deck.py
# author:   Valerie Gadapati
# date:     Feb 12, 2023
# purpose:  to create and manipulate a standard deck of cards, using the card class

from card import *
from random import *

class Deck:
    def __init__(self):
        self.card_list = [Card] * 52  # DONT NEED 52

    def add_standard_cards(self):
        i = 0
        while i <= len(Card.suits) - 1:
            j = 0
            while j <= len(Card.names) - 1:
                card = Card(j, i)
                position = (i * len(Card.names)) + j
                self.card_list[position] = card
                j = j + 1
            i = i + 1

    def shuffle(self):
        i = 0
        while i <= len(self.card_list) - 1:
            current_pos = i
            new_pos = randint(0, len(self.card_list)-1)
            temp = self.card_list[current_pos]
            self.card_list[new_pos] = temp
            i = i + 1

    def deal(self, hand_count):
        hand = []
        i = 0
        while i <= hand_count:
            hand[i] = (self.card_list.pop())
            i = i + 1
        return hand
