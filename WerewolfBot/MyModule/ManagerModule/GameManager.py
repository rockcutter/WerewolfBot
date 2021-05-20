STATUS_NOTACTIVATED =   0x00000000 #ゲーム活性化前
STATUS_RECEPTION =      0x00010000 #ゲーム参加受付中
STATUS_INPROGRESS =     0x00100000 #ゲーム進行中
STATUS_ACCEPTSUPPORTCMD=0x00100001 #ゲーム進行中&サポートコマンド以外受け付けない
STATUS_ACCEPTROLECMD =  0x00100010 #ゲーム進行中&ロール系コマンドのみ受付

class GameManager(object):
    """Gameの進行を管理する"""
    gameStatus = STATUS_NOTACTIVATED
    gameTime = None


    def __init__(self):
        self.ManuInit()
        return

    def ManuInit(self):
        self.gameStatus = STATUS_NOTACTIVATED
        self.gameTime = 0b00000001#最下位ビットが1で夜 初期化は0日目夜
        return

    def CheckStatus(self):
        return self.gameStatus
    #Time関連メソッド----------------------------------
    def TimePasses(self):
        self.gameTime += 1
        return

    def GetDay(self):
        return self.gameTime>> 1

    def GetDayPhase(self):
        return self.gameTime & 0b00000001

    #status変更メソッド--------------------------------
    def ActivateGame(self):
        self.gameStatus = STATUS_RECEPTION
        return

    def StartGame(self):
        self.gameStatus = STATUS_INPROGRESS
        return

    def LimitCommand(self):
        self.gameStatus = STATUS_ACCEPTSUPPORTCMD
