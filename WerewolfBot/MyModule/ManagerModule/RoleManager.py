#管理クラス
import random

from MyModule.RoleModule import role
from MyModule.RoleModule import villager
from MyModule.RoleModule import werewolf


class RoleManager(object):
    """ロール管理全般"""

    allRoleList = []
    roleObjList = []
    villageRoleCount = 0 
    wolfRoleCount = 0
    roleCount = 0

    def __init__(self):
        """コンストラクタ"""
        self.ManuInit()
        return
    
    def ManuInit(self):
        """手動初期化の際に呼び出し"""
        self.allRoleList = [villager.villager(), werewolf.werewolf()]
        self.roleObjList = []
        self.villageRoleCount = 0
        self.wolfRoleCount = 0
        self.roleCount = 0
        return

    def LoadAllRoleList(self):
        return self.allRoleList

    #ランダム化されたロールリストを返す
    def LoadRandomizedRoleObjList(self):
        random.shuffle(self.roleObjList)
        return self.roleObjList

    #生存中のロール数を返す処理-------------------------------------
    def LoadVillageRoleCount(self):
        return self.villageRoleCount

    def LoadWolfRoleCount(self):
        return self.wolfRoleCount

    def LoadRoleCount(self):
        return self.roleCount

    #ロール登録処理--------------------------------------------------
    def AppendRole(self,roleObj):
        self.roleObjList.append(roleObj)
        if(roleObj.side == role.SIDE_VILLAGER):
            self.villageRoleCount += 1
            self.roleCount += 1
        if(roleObj.side == role.SIDE_WEREWOLF):
            self.wolfRoleCount += 1
            self.roleCount += 1
        return

    #死亡時処理-----------------------------------------------------
    def VillageDeathProcess(self):
        self.villageRoleCount -= 1
        return

    def WolfDeathProcess(self):
        self.villageRoleCount -= 1
        return

