# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 10:26:35 2020

@author: Malkari Santhosh
"""
#Ram kishore
import itertools
import random
from itertools import combinations
from collections import defaultdict,Counter

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

    a = check_royal_flush(hand)
    if a[0]:
        return 10,a[1]
    
    a = check_straight_flush(hand)   
    if a[0]:
        return 9,a[1]
     
    a = check_four_of_a_kind(hand)
    if a[0]:
        return 8,a[1]
    
    a = check_full_house(hand)
    if a[0]:
        return 7,a[1]
    
    a = check_flush(hand)
    if a[0]:
        return 6,a[1]
    
    a = check_straight(hand)
    if a[0]:
        return 5,a[1]
    
    a = check_three_of_a_kind(hand)
    if a[0]:
        return 4,a[1]
    
    a = check_two_pairs(hand)
    if a[0]:
        return 3,a[1]
    
    a = check_one_pairs(hand)
    if a[0]:
        return 2,a[1]
    
    return 1,'a'  

card_order_dict = {"2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "T":10,"J":11, "Q":12, "K":13, "A":14}

def check_royal_flush(hand):
    values = [i[0] for i in hand]
    a = check_flush(hand)
    b = False
    if set(values) == set(["T","Q","K","J","A"]):
        b = True   
    if a[0] and b:
        return [True,hand]
    return [False]

    
def check_straight_flush(hand):
    a = check_flush(hand)
    b = check_straight(hand)
    if a[0] and b[0]:
        return [True,hand]
    else:
        return [False]

def check_four_of_a_kind(hand):
    
    values = [i[0] for i in hand]
    value_counts = defaultdict(lambda:0)
    for v in values: 
        value_counts[v]+=1
    if sorted(value_counts.values()) == [1,4]:
        return [True,hand]
    return [False]

def check_full_house(hand):
    values = [i[0] for i in hand]
    value_counts = defaultdict(lambda:0)
    for v in values:
        value_counts[v]+=1
    if sorted(value_counts.values()) == [2,3]:
        return [True,hand]
    return [False]

def check_flush(hand):
    suits = [i[1] for i in hand]
    if len(set(suits))==1:
        return [True,hand]
    else:
        return [False]

def check_straight(hand):
    
    values = [i[0] for i in hand]
    value_counts = defaultdict(lambda:0)
    for v in values:
        
        value_counts[v] += 1
    rank_values = [card_order_dict[i] for i in values]
    value_range = max(rank_values) - min(rank_values)
    if len(set(value_counts.values())) == 1 and (value_range==4):
        return [True,hand]
    else: 
        #check straight with low Ace
        if set(values) == set(["A", "2", "3", "4", "5"]):
            return [True,hand]
        return [False]

def check_three_of_a_kind(hand):
    
    values = [i[0] for i in hand]
    value_counts = defaultdict(lambda:0)
    for v in values:
        
        value_counts[v]+=1
    if set(value_counts.values()) == set([3,1]):
        return [True,hand]
    else:
        return [False]

def check_two_pairs(hand):
    
    values = [i[0] for i in hand]
    value_counts = defaultdict(lambda:0)
    for v in values:
        
        value_counts[v]+=1
    if sorted(value_counts.values())==[1,2,2]: 
        return [True,hand]
    else:
        return [False]

def check_one_pairs(hand):
    values = [i[0] for i in hand]
    value_counts = defaultdict(lambda:0)
    for v in values:
        value_counts[v]+=1
    if 2 in value_counts.values():
        return [True,hand]
    else:
        return [False]

hand_dict = {10:"royal-flush", 9:"straight-flush", 8:"four-of-a-kind", 7:"full-house", 6:"flush", 5:"straight", 4:"three-of-a-kind", 3:"two-pairs", 2:"one-pair", 1:"highest-card"}

def two_pairs(a,two,five,cards):
    
    if card_order_dict[two[0][0]] >  card_order_dict[two[1][0]]:
        d = two[0]
        two[0] = two[1]
        two[1] = d
        
    lis = []
    f = 0

    for i in range(len(cards)):
        for j in range(i+1,len(cards)):
            if(cards[i][0] == cards[j][0]):
                if (cards[i] not in lis):
                    lis.append(cards[i])
                if (cards[j] not in lis):
                    lis.append(cards[j])
                    
    for i in range(len(lis)):
        for j in range(i+1,len(lis)):
            if card_order_dict[lis[j][0]] >  card_order_dict[lis[i][0]]:
                d = lis[j]
                lis[j] = lis[i]
                lis[i] = d
                
    for i in lis:
        if i in cards:
            cards.remove(i)
            
    for i in range(len(cards)):
        for j in range(i+1,len(cards)):
            if card_order_dict[cards[j][0]] >  card_order_dict[cards[i][0]]:
                d = cards[j]
                cards[j] = cards[i]
                cards[i] = d
    f=0

    lis = lis + cards[0:1]
    for i in two:
        if i not in lis:
            f +=1
    if f == 2:
        lis.remove(lis[-1])
        lis.append(two[-1])
    return lis 
    pass

def one_pair(a,two,five,cards):
    #mini = card_order_dict[two[-1]]
    twovalues = [i[0] for i in two]
    fivevalues = [i[0] for i in five]
    cardvalues = [i[0] for i in cards]
    value_counts = defaultdict(lambda:0)
    for v in cards:
        value_counts[v[0]] += 1
    for v in cards:
        if value_counts[v[0]] == 2:
            myval = v
            break
    lis = []
    f = 0
    d ='a'

    for i in range(len(cards)):
        for j in range(i+1,len(cards)):
            if(cards[i][0] == cards[j][0]):
                lis.append(cards[i])
                lis.append(cards[j])
                f =1
                break
        if f == 1:
            break
    for i in range(len(cards)):
        if v[0] == cards[i][0]:
            cards.remove(cards[i])
            break
    for i in range(len(cards)):
        if v[0] == cards[i][0]:
            cards.remove(cards[i])
            break
    for i in range(len(cards)):
        for j in range(i+1,len(cards)):
            if card_order_dict[cards[j][0]] >  card_order_dict[cards[i][0]]:
                d = cards[j]
                cards[j] = cards[i]
                cards[i] = d
    f=0

    lis = lis + cards[:3]
    for i in two:
        if i not in lis:
            f +=1
    if f == 2:
        lis.remove(lis[-1])
        lis.append(two[-1])
    return lis                

            
#exhaustive search using itertools.combinations
def play(cards):
    two = cards[0:2]
    five = cards[2:7]
    five.sort(reverse=True)
    two.sort(reverse=True)
    best_hand = 0
    bestval = 0
    possible_combos = combinations(cards, 5)
    for c in possible_combos: 
        current_hand = list(c)
        current_hand.sort(reverse=True)
        hand_value,best = check_hand(current_hand)
        if hand_value == best_hand:
            a.append(best)
        if hand_value > best_hand:
            a = []
            a.append(best)
            best_hand = hand_value
    if best_hand == 1:
        a = five[0:3]+two
    #my change
    cards.sort()
    if best_hand == 2:
        a = one_pair(a,two,five,cards)
    if best_hand == 3:
        a = two_pairs(a,two,five,cards)
        
    return hand_dict[best_hand],a
