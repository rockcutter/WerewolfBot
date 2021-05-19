#管理クラス

import MyModule.PlayerModule.player

class PlayerManager():
    """全プレイヤーとその属性を管理するクラス"""

    playerClassList = []
    playerDataObjList = []


    def __init__(self):
        playerClassList = []
        playerDataObjList = []
        return

    def AppendPlayer(self,playerDataObj):
        self.playerClassList.append(playerDataObj)
        return

    def IsPlayer(self,argObj):
        """playerObjが一致するプレイヤーは参加しているかTrue/Flase"""
        for tempPlCls in self.playerClassList:
            if(tempPlCls.playerObj == argObj):
                return True

        return False
