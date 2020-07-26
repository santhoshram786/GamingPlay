# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 10:26:35 2020

@author: Malkari Santhosh
"""
import itertools
import random
from itertools import combinations
from collections import defaultdict

list_of_all_cards = []
#Shuffule the cards
def shuff():  
    vals = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
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
  
def check_hand(hand):
    
    if check_straight_flush(hand):
        return 9
     
    if check_four_of_a_kind(hand):
        return 8
     
    if check_full_house(hand):
        return 7
     
    if check_flush(hand):
        return 6
     
    if check_straight(hand):
        return 5
     
    if check_three_of_a_kind(hand):
        return 4
     
    if check_two_pairs(hand):
        return 3
     
    if check_one_pairs(hand):
        return 2
    return 1   

card_order_dict = {"2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "T":10,"J":11, "Q":12, "K":13, "A":14}

def reuse_check_flush(hand):
    suits = [i[1] for i in hand]
    if len(set(suits))==1: 
        return True
    else:
        return False

def reuse_check_straight(hand):
    
    values = [i[0] for i in hand]
    value_counts = defaultdict(lambda:0)
    for v in values:
        
        value_counts[v] += 1
    rank_values = [card_order_dict[i] for i in values]
    value_range = max(rank_values) - min(rank_values)
    if len(set(value_counts.values())) == 1 and (value_range==4): 
        return True
    else: 
        #check straight with low Ace
        if set(values) == set(["A", "2", "3", "4", "5"]):
            print(hand) 
            return True
        return False
    
def check_straight_flush(hand):
    
    if reuse_check_flush(hand) and reuse_check_straight(hand):
        print('9',hand) 
        return True
    else:
        return False

def check_four_of_a_kind(hand):
    
    values = [i[0] for i in hand]
    value_counts = defaultdict(lambda:0)
    for v in values: 
        value_counts[v]+=1
    if sorted(value_counts.values()) == [1,4]:
        print('8',hand) 
        return True
    return False

def check_full_house(hand):
    values = [i[0] for i in hand]
    value_counts = defaultdict(lambda:0)
    for v in values:
        value_counts[v]+=1
    if sorted(value_counts.values()) == [2,3]:
        print('7',hand) 
        return True
    return False

def check_flush(hand):
    suits = [i[1] for i in hand]
    if len(set(suits))==1:
        print('6',hand) 
        return True
    else:
        return False

def check_straight(hand):
    
    values = [i[0] for i in hand]
    value_counts = defaultdict(lambda:0)
    for v in values:
        
        value_counts[v] += 1
    rank_values = [card_order_dict[i] for i in values]
    value_range = max(rank_values) - min(rank_values)
    if len(set(value_counts.values())) == 1 and (value_range==4):
        print('5',hand) 
        return True
    else: 
        #check straight with low Ace
        if set(values) == set(["A", "2", "3", "4", "5"]):
            print('5A',hand) 
            return True
        return False

def check_three_of_a_kind(hand):
    
    values = [i[0] for i in hand]
    value_counts = defaultdict(lambda:0)
    for v in values:
        
        value_counts[v]+=1
    if set(value_counts.values()) == set([3,1]):
        print('4',hand) 
        return True
    else:
        return False

def check_two_pairs(hand):
    
    values = [i[0] for i in hand]
    value_counts = defaultdict(lambda:0)
    for v in values:
        
        value_counts[v]+=1
    if sorted(value_counts.values())==[1,2,2]:
        print('3',hand) 
        return True
    else:
        return False

def check_one_pairs(hand):
    values = [i[0] for i in hand]
    value_counts = defaultdict(lambda:0)
    for v in values:
        value_counts[v]+=1
    if 2 in value_counts.values():
        print('2',hand) 
        return True
    else:
        return False

hand_dict = {9:"straight-flush", 8:"four-of-a-kind", 7:"full-house", 6:"flush", 5:"straight", 4:"three-of-a-kind", 3:"two-pairs", 2:"one-pair", 1:"highest-card"}

#exhaustive search using itertools.combinations
def play(cards):
    hand = cards[:2]
    deck = cards[2:]
    best_hand = 0
    for i in range(6):
        possible_combos = combinations(hand, 5-i)
        for c in possible_combos: 
            current_hand = list(c) + deck[:i]
            hand_value = check_hand(current_hand)
            if hand_value > best_hand:
                best_hand = hand_value      
    return hand_dict[best_hand]

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