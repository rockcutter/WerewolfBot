#管理クラス

from MyModule.RoleModule import role
from MyModule.RoleModule import villager
from MyModule.RoleModule import werewolf

class RoleManager(object):
    """ロール管理全般"""

    roleTemplateList = []
    roleObjList = []
    villageRoleCount = 0 
    wolfRoleCount = 0

    def __init__(self):
        """コンストラクタ"""
        self.ManuInit()
        return
    
    def ManuInit(self):
        """手動初期化の際に呼び出し"""
        roleTemplateList = [villager.villager(), werewolf.werewolf()]
        self.roleObjList = []
        villageRoleCount = 0
        wolfRoleCount = 0
        return

    #ロール登録処理--------------------------------------------------
    def AppendRole(self,roleObj):
        self.roleObjList.append(roleObj)
        if(roleObj.side = role.SIDE_VILLAGER):
            self.villageRoleCount += 1
        if(roleObj.side = role.SIDE_WEREWOLF):
            self.wolfRoleCount += 1
        return

    #死亡時処理-----------------------------------------------------
    def VillageDeathProcess(self):
        self.villageRoleCount -= 1
        return

    def WolfDeathProcess(self):
        self.villageRoleCount -= 1
        return