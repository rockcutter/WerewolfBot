#管理クラス

import MyModule.PlayerModule.player

class PlayerManager():
    """全プレイヤーとその属性を管理するクラス"""

    playerClassList = []
    playerCount = 0


    def __init__(self):
        playerClassList = []
        playerCount = 0
        return

    def AppendPlayer(self,playerDataObj):
        self.playerClassList.append(playerDataObj)
        self.playerCount += 1
        return

    def IsPlayer(self,argObj):
        """playerObjが一致するプレイヤーは参加しているかTrue/Flase"""
        for tempPlCls in self.playerClassList:
            if(tempPlCls.playerObj == argObj):
                return True

        return False

    def ApplyRole(self,roleObjList):
        for i in range(len(self.playerClassList)):
            self.playerClassList[i].RegisterRole(roleObjList[i])
        return

    def LoadPlayerClassList(self):
        return self.playerClassList

    def LoadPlayerCount(self):
        return self.playerCount