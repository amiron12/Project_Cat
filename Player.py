
class Info:
    def __init__(self, name:str, id:int, cards:list):
        self.playerName = name.capitalize()
        self.playerID = id
        self.playerHand = cards
        self.didCall = False

    def player_data(self):
        print(f"Name - {self.playerName}\nID - {self.playerID}\nHand - {self.playerHand}")

    def showSides(self):
            print(self.playerHand[0],self.playerHand[-1])

    def handSum(self):
        total = 0
        for c in self.playerHand:
            if type(c) == str:
                total+=9
            else:
                total+=c
        return total

    def cards(self):
        return f"{self.playerHand[0]}, {self.playerHand[1]}, {self.playerHand[2]}, {self.playerHand[3]}"