# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 10:26:35 2020

@author: Malkari Santhosh
"""
import itertools
import random

list_of_all_cards = []
#Shuffule the cards
def shuff():  
    vals = ['02', '03', '04', '05', '06', '07', '08', '09', '10', 'JACK', 'QUEEN', 'KING', 'ACE']
    suits = ['♠', '♦', '♥', '♣']
    deck = list(itertools.product(vals, suits))
    random.shuffle(deck)
    for val, suit in deck:
        return val+''+suit;
    
#checkif the cards are repeated or not
def check(list_of_all_cards,card):
    if card in list_of_all_cards:
        return True
    return False

#It gives cards foreach player
def pokerMaster(n):
    cards =[]
    global list_of_all_cards;
    while(True):
        card=shuff()
        if(check(list_of_all_cards,card)):
            continue
        cards.append(card)
        list_of_all_cards.append(card)
        if(len(cards)==n):
            break
    return cards

#Functions for poker strength
#1.
def royal_flush(strength_cards):
    strength_cards.sort(reverse=True)
    print(strength_cards)
    if strength_cards[0][0] != 'Q':
        return False
    elif strength_cards[1][0] != 'K':
        return False
    elif strength_cards[2][0] != 'J':
        return False
    elif strength_cards[3][0] != 'A':
        return False
    elif strength_cards[4][0] != '1':
        return False
    suite = strength_cards[0][-1]
    for i in range(len(strength_cards)-2):
        if suite != strength_cards[i][-1]:
            return False
    return True

#2.
def straight_flush():
    pass

#3.
def four_of_a_kind():
    pass

#4.
def full_house():
    pass

#5.
def flush(p):
    a = p[0][-1]
    c = 0
    for i in range(len(p)):
        if a == p[i][-1]:
            c+=1
    if c < 5 :
        return False
    return True

#6.
def straight():
    pass

#7.
def three_of_a_kind():
    pass

#8.
def two_pair(p):
    p.sort()
    pass

#9.
def one_pair():
    pass

#10.
def high_card():
    pass
