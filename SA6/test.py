# filename: test.py
# author:   Valerie Gadapati
# date:     Feb 12, 2023
# purpose:  driver code for the deck and card classes

from deck import *

card = Card(5, 1)
# prints "5 of clubs"
print(card)

card = Card(12, 4)
# prints "Queen of hearts"
print(card)

print("----")

deck = Deck()
# Add the 52 standard cards to the new deck
deck.add_standard_cards()

# Reorder the cards in the deck randomly.
#  The shuffle method makes use of the randint function
deck.shuffle()

# Create a new tiny Deck of cards called hand, made up
#   of the last five cards in deck.  The deal method should
#   also remove those last five cards from "deck".
hand = deck.deal(5)

# print the cards in the hand
# Note that the hand is not a list of cards, it is a reference of a Deck object.
for card in hand.card_list:
    print(card)

print("----")

# print the remaining cards in the deck
for card in deck.card_list:
    print(card)
