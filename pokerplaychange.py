from pokerFunctions import pokerModules
import random

card_order_dict = {"2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "T":10,"J":11, "Q":12, "K":13, "A":14}
hand_dict = {10:"royal-flush", 9:"straight-flush", 8:"four-of-a-kind", 7:"full-house", 6:"flush", 5:"straight", 4:"three-of-a-kind", 3:"two-pairs", 2:"one-pair", 1:"highest-card"}
def ifdoublewinner(p,main):
        
    if p == 5:
        return main
    
    if len(main) == 1:
        return main
    
    else:
        best_hand = main[0][-1][p][0]
        if len(best_hand)>1:
            best_hand = best_hand[0]
        main1 = []
        for i in range(0,len(main)):
            hand_value = main[i][-1][p][0]
            if len(hand_value)>1:
                hand_value = hand_value[0]

            if card_order_dict[hand_value] == card_order_dict[best_hand]:
                main1.append(main[i])
            if card_order_dict[hand_value] > card_order_dict[best_hand]:
                main1 = []
                main1.append(main[i])
                best_hand = hand_value
        return ifdoublewinner(p+1,main1)

                   
#Player count
while True:
    numberOfPlayers=int(input('enter the palyer count:'))
    if numberOfPlayers > 2 and numberOfPlayers < 10:
        break
    
player=[]
names = ['**RAM**','**KISHORE**','**JHON**','**MANI**','**ROBERT**','**HARRY**','**MANJU**','**MANNY**','**JONNY**']
entered_names = []
loop_var_for_names = 0
check = []                                         #check of each player
play_amount=[]                                     #Each player bet amount
aftercards = False                                 #To know the player who played after cards reveled

while (loop_var_for_names < numberOfPlayers):
    name=random.choice(names)                      #setting names to players
    if name in entered_names:
        continue
    entered_names.append(name)
    player.append([name,100])                      #setting amounts 100rs each
    loop_var_for_names += 1
    
for i in range(numberOfPlayers):                   #Displaying amounts
    print(player[i][0],'has amount',player[i][1])

who_starts = 0
players = tuple(player)
plaer = players

while(True):
    
    flopcount = 3                                           #To take 1st 3 cards
    player = list(players)                                  #players list for playing with same people
    sample_FTR = []                                         #lis of 5 cards at beginning it is emtpy
    
    for gamer in range(numberOfPlayers):                    #Getting cards to players
        player[gamer].append(pokerModules.pokerMaster(2))
        check.append(False)                                 #set check to false for each player
        play_amount.append(0)                               #set all spend amounts to 0
        
    Flop_Turn_River=pokerModules.pokerMaster(5)             #getting 5 cards
    
    for gamer in range(numberOfPlayers):
        print('Player',gamer+1,'cards--->',player[gamer][0],player[gamer][1],player[gamer][-1])  #Displaying player name money cards
    print("**************************************************&&")
    print('Flop,Turn and River cards--->',*Flop_Turn_River) #Displaying 5 cards
    print("**************************************************&&")

    print("Selection")
    for i in range(numberOfPlayers):
        a,b = pokerModules.play(player[i][-1]+Flop_Turn_River)
        print('Player',i+1,'--',hand_dict[a],b)
        
    while True:
        count = numberOfPlayers                             #storing players count
        get_amount = 0                                      #sum of amounts of all players
        amount = 0                                          #Entering raising amount
        who_starts = who_starts%count
        player[who_starts][1] -= 10                         #1st person to bet 10rs
        play_amount[who_starts] += 10
        print(player[who_starts][0],"Kept 10 Rs")
        
        who_starts += 1
        who_starts = who_starts%count
        player[who_starts][1] -= 20                         #2nd person to bet 10rs
        play_amount[who_starts] += 20
        print(player[who_starts][0],"Kept 20 Rs")
        
        next_one = who_starts+1                             #Next player(3rd person)
        
        while True:
            raised = False                                  #raised kept false
            aftercards = False
            next_one = next_one%count                       #Next player
            
            print(player[next_one][0],"please Select any of the one of three options")
            print("\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n")
            print(player[next_one][0],',you have amount',player[next_one][1])                   #PLAYER AMOUNT
            print("\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n")
            
            #selection of Fold Call Raise
            print("Press 1 for FOLD , 2 for Call(Amount should be = ",max(play_amount)-play_amount[next_one],")"," , 3 for RAISE(Amount should be > ",max(play_amount)-play_amount[next_one],"): ",end="")
            inputt = input()
            if inputt not in ['1','2','3']:    #checking if correct opion is entered or not
                print("Enter correct option")
                continue
            
            if inputt == '1':                               #Fold option
                player.remove(player[next_one])             #Removing the player from player list
                play_amount.remove(play_amount[next_one])   #Removing the player amount from play_amount list
                a = check.pop(next_one)               #Removing the player check from check list
                count -= 1                                  #Decrementing players count
                next_one -= 1                               
                
            elif inputt == '2':                             #Call option
                check[next_one] = True                      #check of player set true                 
                maxi = max(play_amount)
                if play_amount[next_one] < maxi :           #Calculaing amount to check
                    amou = maxi-play_amount[next_one]
                    play_amount[next_one] += amou
                    player[next_one][1] -= amou             #removing amount from his wallet
                
            elif inputt == '3':                             #Raise opion
                if player[next_one][1] <= 0:
                    prin(player[next_one][0],"You Wallet is empty")         #0 amount in player wallett
                    continue
                while True:
                    raised = True                                           #Raised true
                    amount = int(input("Enter your amount to raise(only integer value:"))
                    if amount <= player[next_one][1] and amount > max(play_amount)-play_amount[next_one]:                       #Checking for right entered amount
                        check_amou = amount + play_amount[next_one]
                        play_amount[next_one] += amount
                        player[next_one][1] -= amount
                        print(play_amount)
                        
                        if check_amou == max(play_amount):                  #checking player kept amount = max amount or not
                            check[next_one]=True                            #if yes TRUE
                            
                        for gamer in range(count):
                            if gamer == next_one:
                                continue
                            check[gamer]=False
                        break
                    print("Check your amount and status  enter again---")
                    
            print(check)                                                            #Printing check
            if not raised:                
                if all(check):
                    print("Checking.................")
                    for gamer in range(count):                                  #Displaying amounts
                        print(player[gamer][0],'cards are',player[gamer][-1])
                        
                    if len(sample_FTR) == 5:                                        #Checking end of play
                        if len(player) == 1:  #if all player(except one) set to fold
                            print(player[0][0],"won the match")
                        break
                    
                    if flopcount == 0:          #taking ou last card in 5 cards
                        sample_FTR = Flop_Turn_River
                        print("************************************")
                        print("* Cards are: ",Flop_Turn_River,"*")
                        print("************************************")
                        
                    if flopcount == 1:          #taking ou next card in 5 cards
                        sample_FTR = Flop_Turn_River[:4]
                        print("************************************")
                        print("* Cards are: ",Flop_Turn_River[:4],"*")
                        print("************************************")
                        flopcount = 0
                        
                    if flopcount == 3:          #taking ou 1st 3 cards in 5 cards
                        sample_FTR = Flop_Turn_River[:3]
                        print("************************************")
                        print("* Cards are: ",Flop_Turn_River[:3],"*")
                        print("************************************")
                        flopcount = 1           #to take the next step
                        
                    for gamer in range(count):   #All players check to False
                        check[gamer]=False
                        
                    get_amount += sum(play_amount)  #sum of amounts of all players
                    
                    print("AMOUNT COLLECTED IS :",sum(play_amount))  #printing collected amount until for all check
                    print("Total AMOUNT COLLECTED IS :",get_amount)  #Total amount for whole game
                    
                    for i in range(count): #amounts set to 0
                        play_amount[i]=0
                    aftercards = True
                    next_one = who_starts-1
                    if who_starts-1 < 0:
                        next_one = count-1
        
            if len(player) == 1:  #if all player(except one) set to fold
                our_hand,mainlist = pokerModules.play(player[i][-1]+Flop_Turn_River)
                print(player[0][0],"won the match")
                break
            if not aftercards:
                next_one += 1  #increment to next player
        break
    
    best_hand = 0
    for i in range(numberOfPlayers):#count):
        our_hand,mainlist = pokerModules.play(player[i][-1]+Flop_Turn_River)
        if our_hand == best_hand:
            player[i].append(mainlist)
            main.append(player[i])
        if our_hand > best_hand:
            main = []
            player[i].append(mainlist)
            main.append(player[i])
            best_hand = our_hand

    if len(main) == 1:
        print("-------------------------------------------------------------------------------------------------------------------------------------")
        print('Player',main,"won the match by",hand_dict[best_hand])
        print("-------------------------------------------------------------------------------------------------------------------------------------")
    else:
        mai = ifdoublewinner(0,main)
        print("-------------------------------------------------------------------------------------------------------------------------------------")
        for i in mai:
            print(i[0],i[1],i[-2],i[-1],"won the match by",hand_dict[best_hand])
        print("-------------------------------------------------------------------------------------------------------------------------------------")
    
    while True:
        select = input("if you continue with same players enter 1 or else 0: ") #selecting to play with same players or not
        if select == '1' or select == '0':
            break
    if select == '1':
        pokerModules.list_of_all_cards=[]  #list of all cards set to empty
        continue
    else :
        break

    break
     
    



