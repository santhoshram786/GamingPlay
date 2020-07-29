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
check = []
play_amount=[]
while (loop_var_for_names < numberOfPlayers):
    name=random.choice(names)
    if name in entered_names:
        continue
    entered_names.append(name)
    player.append([name,100])
    loop_var_for_names +=1
    
for i in range(numberOfPlayers):
    print(player[i][0],'has amount',player[i][1])

who_starts = 0
players = tuple(player)
plaer = players
while(True):
    flopcount = 3
    player = list(players)
    sample_FTR = []
    
    for gamer in range(numberOfPlayers):
        player[gamer].append(pokerModules.pokerMaster(2))
        check.append(False)
        play_amount.append(0)
        
    Flop_Turn_River=pokerModules.pokerMaster(5)
    
    for gamer in range(numberOfPlayers):
        print('Player',gamer+1,'cards--->',*player[gamer])
    print('Flop,Turn and River cards--->',*Flop_Turn_River)
    
    while True:
        count = numberOfPlayers
        get_amount = 0
        amount = 0
        who_starts = who_starts%count
        player[who_starts][1] -= 10
        play_amount[who_starts] += 10
        print(player[who_starts][0],"Kept 10 Rs")
        
        who_starts += 1
        who_starts = who_starts%count
        player[who_starts][1] -= 20
        play_amount[who_starts] += 20
        print(player[who_starts][0],"Kept 20 Rs")
        
        next_one = who_starts+1
        
        while True:
            raised = False
            next_one = next_one%count
            if next_one == (who_starts+1)%count:
                print("\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n")
                for j in range(count):
                    print(player[j][0],'has amount',player[j][1])
                print("\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n")
            print(player[next_one][0],"please Select any of the one of three options")
            print("Press 1 for FOLD , 2 for Call(Amount should be = ",max(play_amount),")"," , 3 for RAISE(Amount should be > ",max(play_amount),"): ",end="")
            inputt = input()
            if inputt not in ['1','2','3']:
                print("Enter correct option")
                continue
            if inputt == '1':
                player.remove(player[next_one])
                play_amount.remove(play_amount[next_one])
                check.remove(check[next_one])
                count -= 1
                next_one -= 1
                
            elif inputt == '2':
                check[next_one] = True
                print(player[next_one][0])
                maxi = max(play_amount)
                if play_amount[next_one] < maxi :
                    amou = maxi-play_amount[next_one]
                    play_amount[next_one] += amou
                    player[next_one][1] -= amou
                
            elif inputt == '3':
                while True:
                    raised = True
                    amount = int(input("Enter your amount to raise(only integer value:"))
                    if amount < 100 and amount <= player[next_one][1]:
                        play_amount[next_one] += amount
                        player[next_one][1] -= amount
                        if amount == max(play_amount):
                            check[next_one]=True
                        for gamer in range(count):
                            if gamer == next_one:
                                continue
                            check[gamer]=False
                        break
                    print("Check your amount and enter again---")
            print(check)       
            if not raised:                
                if all(check):
                    print("Checking.................")
                    if len(sample_FTR) == 5:
                        break
                    if flopcount == 0:
                        sample_FTR = Flop_Turn_River
                        print("Cards are: ",Flop_Turn_River)
                    if flopcount == 1:
                        sample_FTR = Flop_Turn_River[:4]
                        print("Cards are: ",Flop_Turn_River[:4])
                        flopcount = 0
                    if flopcount == 3:
                        sample_FTR = Flop_Turn_River[:3]
                        print("Cards are: ",Flop_Turn_River[:3])
                        flopcount = 1
                    for gamer in range(count):
                        check[gamer]=False
                    get_amount += sum(play_amount)
                    print("AMOUNT COLLECTED IS :",sum(play_amount))
                    print("Total AMOUNT COLLECTED IS :",get_amount)
                    for i in range(count):
                        play_amount[i]=0
        
            if len(player) == 1:
                print(player[0][0],"won the match")
                break
            next_one += 1
        break
    while True:
        select = input("if you continue with same players enter 1 or else 0: ")
        if select == '1' or select == '0':
            break
    if select == '1':
        pokerModules.list_of_all_cards=[]
        continue
    else :
        break
          
    print("Selection")
    for i in range(numberOfPlayers):
        print('Player',i+1,'--',pokerModules.play(player[i][-1]+Flop_Turn_River))

    break
     
    



