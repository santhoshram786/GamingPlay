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

    '''if royal_flush(p1+pro):#['KING ♣','QUEEN ♣','ACE ♣','JACK ♣','10 ♣','05 ♠','09 ♠']):
        print('royal_flush')
    else :
        print('Not royal_flush')
            
    if royal_flush(p3+pro):#['KING ♣','QUEEN ♣','ACE ♣','JACK ♣','10 ♣','05 ♠','09 ♠']):
        print('royal_flush')
    else :
        print('Not royal_flush')


        #flush
    if flush(['KING ♣','QUEEN ♣','ACE ♣','JACK ♣','10 ♣','05 ♠','09 ♠']):
        print('flush')
    else :
        print('Not flush')'''
    break
     
    



