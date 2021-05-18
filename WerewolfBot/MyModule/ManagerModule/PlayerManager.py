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


