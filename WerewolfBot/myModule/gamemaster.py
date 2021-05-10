import myModule.game

class gamemaster(myModule.game.game):
    day = None

    def __init__(self):
        self.day = 0b00000000
        return