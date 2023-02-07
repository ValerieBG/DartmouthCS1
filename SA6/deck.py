# filename: deck.py
# author:   Valerie Gadapati
# date:     Feb 12, 2023
# purpose:  to create and manipulate a deck of cards, using the card class

from card import *
from random import *


class Deck:
    # initialize a deck of cards, default length is a standard deck of 52 cards
    def __init__(self, length=52):
        self.card_list = [Card] * length

    # add standard 52 cards consisting of Ace, 2, 3 ... 10, Jack, Queen, King cards within each suit
    def add_standard_cards(self):
        i = 0
        while i < len(Card.suits):
            j = 0
            while j < len(Card.values):
                card = Card(j, i)
                position = (i * len(Card.values)) + j
                self.card_list[position] = card
                j = j + 1
            i = i + 1

    # function to randomly shuffle the deck based on card positions
    def shuffle(self):
        i = 0
        while i < len(self.card_list):
            current_pos = i
            new_pos = randint(0, len(self.card_list) - 1)
            temp = self.card_list[current_pos]
            self.card_list[current_pos] = self.card_list[new_pos]
            self.card_list[new_pos] = temp
            i = i + 1

    # deal a deck of hand_count length, and remove those cards from the original deck
    def deal(self, hand_count):
        dealt = Deck(hand_count)
        i = 0
        while i < len(dealt.card_list):
            dealt.card_list[i] = self.card_list.pop()
            i += 1
        return dealt
