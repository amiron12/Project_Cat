import random
from nis import match
from random import choice
from tracemalloc import take_snapshot

import CardFunctions
import Constants
import Player
import Group
import Group
import Verify


class Deck:

        def __init__(self):
            self.closed_deck = []
            self.closed_deck = Constants.loadDeck(self.closed_deck)
            self.open_deck = []
            random.shuffle(self.closed_deck)

        def deal(self): #dealing 4 random cards, returning a list of those cards
            hand = []
            for _ in range(4):
                hand.append(self.closed_deck.pop())
            return hand

        def takeCard(self, p, playerGroup):
            # initial function when it's a player's turn

            if not self.open_deck: #checking if the open deck is empty
                topCard = "-----"
            else:
                topCard = self.open_deck[-1]

            print(f"--{p.playerName}--:\n"
                  f"1 - Take a card from deck\n"
                  f"2 - Take top card -  {topCard}\n"
                  f"3 - Call end") #calling the end of the game
            choice = Verify.choiceVer(3)
            match choice:
             case 1:
                self.drawDeck(p, playerGroup) # p = the player who is playing right now
             case 2:
                 if not self.open_deck: #checking if the player is trying to take a card from an empty deck
                    Verify.errorPrint()
                    self.takeCard(p, playerGroup)
                 else:
                    self.drawTable(p)
             case 3:
                p.didCall = True #announcing that the player called
                print("\nLAST ROUND!\n")

        def drawDeck(self,p, playerGroup):      # when a player chooses to draw a card from the closed deck
            card = self.closed_deck.pop() #the upmost card on the open deck
            if card == "swap" or card == "Peek" or card == "Pull-Two":# is it a special card
                print(f"--[{card}]--\n Use - 1\n Throw - 2")# if it is - do they want to use it
                choice = Verify.choiceVer(2) #total verification
                if choice == 1: # they want to use it
                    CardFunctions.specialCard(card,p, playerGroup)
                else:self.open_deck.append(card) #player wants to throw the card
            else: # it's not a special card
                print(f"--[{card}]--\n Take - 1\n Throw - 2") #player decides to take or throw the card
                choice = Verify.choiceVer(2)
                if choice == 1: #player wants to take the card
                    print("Choose a card to throw (1-4):") #which of the current hand does he want to throw
                    choice = Verify.choiceVer(4)-1 # the integer received is the index of the card (subtracted by 1 for use)
                    self.open_deck.append(p.playerHand[choice])
                    p.playerHand[choice] = card
                elif choice == 2:  #player throws the card to the open deck
                    self.open_deck.append(card)

        def drawTable(self, p): # when a player chooses to take the card open on the table
            card = self.open_deck.pop()
            print("Choose a card to throw (1-4):") #which of the current hand does he want to throw
            choice = int(input())-1 # the integer received is the index of the card (subtracted by 1 for use)
            self.open_deck.append(p.playerHand[choice])
            p.playerHand[choice] = card

        def takingTwo(self,p,playerGroup):
          for _ in range(2):
            card = self.closed_deck.pop()  # the upmost card on the open deck
            if card == "swap" or card == "Peek" or card == "Pull-Two":  # is it a special card
                print(f"--[{card}]--\n Use - 1\n Throw - 2")  # if it is - do they want to use it
                choice = Verify.choiceVer(2)  # total verification
                if choice == 1:  # they want to use it
                    CardFunctions.specialCard(card, p, playerGroup)
                else:
                    self.open_deck.append(card)  # player wants to throw the card
            else:  # it's not a special card
                print(f"--[{card}]--\n Take - 1\n Throw - 2")  # player decides to take or throw the card
                choice = Verify.choiceVer(2)
                match choice:
                    case 1:  # player wants to take the card
                        print("Choose a card to throw (1-4):")  # which of the current hand does he want to throw
                        choice = Verify.choiceVer(4) - 1  # the integer received is the index of the card (subtracted by 1 for use)
                        self.open_deck.append(p.playerHand[choice])
                        p.playerHand[choice] = card
                        break
                    case 2:  # player throws the card to the open deck
                        self.open_deck.append(card)

