class game(object):
    """ゲーム管理関連のクラス"""
    member = []
    
    def addMember(self,str):
        self.member.append(str)
        return