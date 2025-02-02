import Table

class Data:
    def __init__(self, table):
        self.players = []
        self.table = table

    def size(self):
        return len(self.players)

    def addPlayer(self,p):
        self.players.append(p)

    def showPlayers(self):
        for i in self.players:
            i.player_data()

