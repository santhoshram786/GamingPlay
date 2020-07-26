# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 15:08:51 2020

@author: Malkari Santhosh
"""

from itertools import combinations

hand_dict = {9:"straight-flush", 8:"four-of-a-kind", 7:"full-house", 6:"flush", 5:"straight", 4:"three-of-a-kind", 3:"two-pairs", 2:"one-pair", 1:"highest-card"}

#exhaustive search using itertools.combinations
def play(cards):
    hand = cards[:5]
    deck = cards[5:]
    best_hand = 0
    for i in range(6):
        possible_combos = combinations(hand, 5-i)
        for c in possible_combos: 
            current_hand = list(c) + deck[:i]
            hand_value = check_hand(current_hand)
            if hand_value > best_hand:
                best_hand = hand_value
                
    return hand_dict[best_hand]

play(cards)
