PHASE_RECEPTION = 0b00000000
PHASE_INPROGRESS = 0b10000000

class game(object):
    """ゲーム管理関連のクラス"""
    member = []
    status = PHASE_RECEPTION
    

    def __init__(self):
        self.InitGame()
        return

    def InitGame(self):
        member = []
        status = PHASE_RECEPTION
        return 

    def Start(self):
        if(status & PHASE_INPROGRESS == PHASE_INPROGRESS):
            return False
        status = PHASE_INPROGRESS
        return True

    def Stop(self):
        if(status & PHASE_RECEPTION == PHASE_RECEPTION):
            return False
        status = PHASE_RECEPTION
        self.InitGame()
        return True


    #概要: メンバーを追加する関数
    #引数: メンバーを示す文字列
    #戻り値: 無し
    def AddMember(self,str):
        self.member.append(str)
        return

    