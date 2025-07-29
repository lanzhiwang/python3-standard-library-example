#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2010 Doug Hellmann.  All rights reserved.
#
"""Random choice"""

# end_pymotw_header
import random
import itertools

"""
A simulation of a card game needs to mix up the deck of cards and then deal them to the players,
without using the same card more than once.
Using choice() could result in the same card being dealt twice,
so instead, the deck can be mixed up with shuffle() and then individual cards removed as they are dealt.
模拟纸牌游戏需要将一副牌打散, 然后发给玩家, 并且不能重复使用同一张牌.
使用 choice() 可能会导致同一张牌被发两次, 因此可以使用 shuffle() 打散一副牌, 然后在发牌时将每张牌取出.
"""

FACE_CARDS = ("J", "Q", "K", "A")
SUITS = ("H", "D", "C", "S")


def new_deck():
    return [
        # Always use 2 places for the value, so the strings
        # are a consistent width.
        "{:>2}{}".format(*c)
        for c in itertools.product(
            itertools.chain(range(2, 11), FACE_CARDS),
            SUITS,
        )
    ]


def show_deck(deck):
    p_deck = deck[:]
    while p_deck:
        row = p_deck[:13]
        p_deck = p_deck[13:]
        for j in row:
            print(j, end=" ")
        print()


# Make a new deck, with the cards in order
deck = new_deck()
print("Initial deck:")
show_deck(deck)

# Shuffle the deck to randomize the order
random.shuffle(deck)
print("\nShuffled deck:")
show_deck(deck)

# Deal 4 hands of 5 cards each
hands = [[], [], [], []]

for i in range(5):
    for h in hands:
        h.append(deck.pop())

# Show the hands
print("\nHands:")
for n, h in enumerate(hands):
    print("{}:".format(n + 1), end=" ")
    for c in h:
        print(c, end=" ")
    print()

# Show the remaining deck
print("\nRemaining deck:")
show_deck(deck)

"""
$ python 08_random_shuffle.py
Initial deck:
 2H  2D  2C  2S  3H  3D  3C  3S  4H  4D  4C  4S  5H
 5D  5C  5S  6H  6D  6C  6S  7H  7D  7C  7S  8H  8D
 8C  8S  9H  9D  9C  9S 10H 10D 10C 10S  JH  JD  JC
 JS  QH  QD  QC  QS  KH  KD  KC  KS  AH  AD  AC  AS

Shuffled deck:
 2C  6H  4H 10D  5S  KH  3C  JH  3D  2H 10C  QC  AD
 7C  JD  3S  KD  2S  4S  AC  QD 10S  6C  4C  9S  9H
 8H  5C  QH 10H  JS  6D  JC  3H  9D  7H  2D  QS  KS
 7S  AS  8S  6S  AH  7D  5D  5H  4D  9C  8D  8C  KC

Hands:
1:  KC  4D  AH  7S  7H
2:  8C  5H  6S  KS  9D
3:  8D  5D  8S  QS  3H
4:  9C  7D  AS  2D  JC

Remaining deck:
 2C  6H  4H 10D  5S  KH  3C  JH  3D  2H 10C  QC  AD
 7C  JD  3S  KD  2S  4S  AC  QD 10S  6C  4C  9S  9H
 8H  5C  QH 10H  JS  6D
$
"""
