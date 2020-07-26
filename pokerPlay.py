from pokerFunctions import pokerModules
import re

while True:
    numberOfPlayers=int(input('enter the palyer count:'))
    if numberOfPlayers > 2 and numberOfPlayers < 10:
        break
       
player=[]   
while(True):
    for gamer in range(numberOfPlayers):
        player.append(pokerModules.pokerMaster(2))
    Flop_Turn_River=pokerModules.pokerMaster(5)
    for gamer in range(numberOfPlayers):
        print('Player',gamer+1,'cards--->',*player[gamer])
    print('Flop,Turn and River cards--->',*Flop_Turn_River)
  
    print("Selection")
    for i in range(numberOfPlayers):
        print('Player',i+1,'--',pokerModules.play(player[i]+Flop_Turn_River))
    break
     
    



