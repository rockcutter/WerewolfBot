#管理クラス

class RoleManager(object):
    """ロール管理全般"""

    roleObjList = []
    villageRoleCount = 0 
    wolfRoleCount = 0

    def __init__(self):
        """コンストラクタ"""
        self.roleObjList = []
        villageRoleCount = 0
        wolfRoleCount = 0
        return
    
    def ManuInit(self):
        """手動初期化の際に呼び出し"""
        self.roleObjList = []
        villageRoleCount = 0
        wolfRoleCount = 0
        return

    #ロール登録処理--------------------------------------------------
    def AppendVillageRole(self,roleObj):
        self.roleObjList.append(roleObj)
        self.villageRoleCount += 1
        return

    def AppendWolfRole(self,roleObj):
        self.roleObjList.append(roleObj)
        self.wolfRoleCount += 1
        return

    #死亡時処理-----------------------------------------------------
    def VillageDeathProcess(self):
        self.villageRoleCount -= 1
        return

    def WolfDeathProcess(self):
        self.villageRoleCount -= 1
        return