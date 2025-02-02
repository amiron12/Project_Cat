import os
import time
from random import choice
from turtledemo.penrose import start
import os
import Group
import Player
import Table
import Verify



def setup():
    print("Hello! Welcome to the game - Rat - a - tat - cat, please enter the number of player")
    try:
        numOfPlayers = int(input())
    except:
        Verify.errorPrint()
        setup()
    else:
        table = Table.Deck() #Initilizing a table to play on
        playerGroup = Group.Data(table) #Initilizing a game using the table we set
        for j in range(numOfPlayers):
            name = str(Verify.nameVer())
            p = Player.Info(name, j, playerGroup.table.deal()) #creating a player using the same table associated to the current game
            playerGroup.players.append(p) #Adding said player to the game
        initialCardCheck(playerGroup)

def initialCardCheck(playerGroup):
    #all the players check their cards
    for p in playerGroup.players:
        print(f"---{p.playerName} - Press 'Enter' to see your cards:")
        input()
        p.showSides()

        for k in range(3):
            time.sleep(1)
            print("---", end="")

        for _ in range(20):print()
    mainloop(playerGroup)

def mainloop(playerGroup):
    while len(playerGroup.table.closed_deck)>0: #looping until the closed deck is empty
        for p in playerGroup.players:
            if not p.didCall: # if a player called to end - it will be saved till the next round in his info
                playerGroup.table.takeCard(p, playerGroup)
                for _ in range(5): print()
            else: ending(playerGroup) # a player has called and the game has ended
    ending(playerGroup)

def ending(playerGroup):
    lst = playerGroup.players
    fp = Player.Info("name", 000, [9,9,9,9]) # fictional player only for the first loop
    lead = [fp]
    for p in lst:
        if p.handSum() == lead[0].handSum(): # checking if there is a tie
            lead.append(p)
        if p.handSum() < lead[0].handSum(): # if there is a smaller hand - lead players are deleted
            lead.clear()
            lead.append(p)
    length = len(lead)
    match length:
         case 1: #checking if there is only one winner or ties
            print(f"The winner is {lead[0].playerName} with: {lead[0].cards()}")
         case 2:
            print(f"The tied winners are {lead[0].playerName} with: {lead[0].cards()}, and {lead[1].playerName} with: {lead[1].cards()}")
         case 3:
            print(f"The tied winners are {lead[0].playerName}, {lead[0].cards()} and {lead[1].playerName} with card sum of: {lead[1].handSum()}")
         case 4:
            print(f"Wow, everybody is tied with a card sum of - {lead[0].handSum()}")

    print(f"\nThank you for playing!\n"
          f"1 - Start a new game\n"
          f"2 - Exit\n"
          f"3 - See all player's hands")
    choice = Verify.choiceVer(3)
    match choice:
        case 1: setup() #starting a new game
        case 2: exit()
        case 3: playerGroup.showPlayers()


setup() # * Game Start *