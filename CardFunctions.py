import time

def specialCard(type:str, p, playerGroup):
    if  type == "swap":swap(p,playerGroup)
    elif type == "Peek":peek(p)
    elif type == "Pull-Two":pullTwo(p,playerGroup)

def pullTwo(p, playerGroup):
        playerGroup.table.takingTwo(p, playerGroup)

def peek(p):
    print("Which card do you want to peek?(1-4)")
    choice = int(input())-1
    print(p.playerHand[choice])
    for k in range(3):
        time.sleep(1)
        print("---", end="")

def swap(p,playerGroup):
    print(f"Which of your cards do you want to swap?(1-4):")
    mycard = int(input())-1 #the card he wants to swap
    print("Which player do you want to swap with?")
    num = 1
    templist=[]
    for i in playerGroup.players:
        if i.playerID!=p.playerID:
            templist.append(i)
            print(f"{num} - {i.playerName}")
            num+=1
    playerSwap = int(input())-1 #the player which he wants to swap with
    print(f"Choose a card from {templist[playerSwap].playerName}'s hand (1-4):")
    cardchoice = int(input())-1 #the other player's card he wants to take
    myswap = p.playerHand[mycard] # temporary variable of the card i give
    hisswap = templist[playerSwap].playerHand[cardchoice] #temporary variable of the card i take
    p.playerHand[mycard] = hisswap
    templist[playerSwap].playerHand[cardchoice] = myswap
    print(f"You got --[{hisswap}]--")
    for k in range(3):
        time.sleep(1)
        print("---", end="")
