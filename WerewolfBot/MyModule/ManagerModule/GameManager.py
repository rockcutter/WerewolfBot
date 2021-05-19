STATUS_NOTACTIVATED =   0x00000000
STATUS_RECEPTION =      0x00010000
STATUS_INPROGRESS =     0x00100000


class GameManager(object):
    """Gameの進行を管理する"""
    gameStatus = NOTACTIVATED

    def __init__(self):
        self.ManuInit()
        return

    def ManuInit(self):
        self.gameStatus = NOTACTIVATED
        return

    def CheckStatus(self):
        return self.gameStatus

    #status変更メソッド--------------------------------
    def ActivateGame(self):
        self.gameStatus = STATUS_RECEPTION
        return

    def StartGame(self):
        self.gameStatus = STATUS_INPROGRESS
        return


