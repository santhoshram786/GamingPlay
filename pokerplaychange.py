from pokerFunctions import pokerModules
import random

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
        print('Player',gamer+1,'cards--->',*player[gamer])  #Displaying player name money cards
    print('Flop,Turn and River cards--->',*Flop_Turn_River) #Displaying 5 cards

    print("Selection")
    for i in range(numberOfPlayers):
        print('Player',i+1,'--',pokerModules.play(player[i][-1]+Flop_Turn_River))
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
                check.remove(check[next_one])               #Removing the player check from check list
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
                        print("Cards are: ",Flop_Turn_River)
                        
                    if flopcount == 1:          #taking ou next card in 5 cards
                        sample_FTR = Flop_Turn_River[:4]
                        print("Cards are: ",Flop_Turn_River[:4])
                        flopcount = 0
                        
                    if flopcount == 3:          #taking ou 1st 3 cards in 5 cards
                        sample_FTR = Flop_Turn_River[:3]
                        print("Cards are: ",Flop_Turn_River[:3])
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
                print(player[0][0],"won the match")
                break
            if not aftercards:
                next_one += 1  #increment to next player
        break
    while True:
        select = input("if you continue with same players enter 1 or else 0: ") #selecting to play with same players or not
        if select == '1' or select == '0':
            break
    if select == '1':
        pokerModules.list_of_all_cards=[]  #list of all cards set to empty
        continue
    else :
        break
          
    print("Selection")
    for i in range(numberOfPlayers):
        print('Player',i+1,'--',pokerModules.play(player[i][-1]+Flop_Turn_River))

    break
     
    



