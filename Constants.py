def loadDeck(closedDeck:list):
    for i in range(9):
        for _ in range(4):
            closedDeck.append(i)
    for _ in range(4):
        closedDeck.extend(["swap", "Peek", "Pull-Two"])
    return closedDeck