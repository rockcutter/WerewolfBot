PHASE_RECEPTION = 0b00000000
PHASE_INPROGRESS = 0b10000000

class game(object):
    """ゲーム管理関連のクラス"""
    member = []
    status = PHASE_RECEPTION
    

    def __init__(self):
        status = PHASE_RECEPTION
        return

    def Start(self):
        if(status & PHASE_INPROGRESS == PHASE_INPROGRESS):
            return False
        status = PHASE_INPROGRESS
        return True

    

    def AddMember(self,str):
        self.member.append(str)
        return

    