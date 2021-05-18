import myModule.roles.role

class villager(myModule.roles.role.role):
    """description of class"""

    def __init__(self):
        """
        コンストラクタ
        Args:
            argGuild: データ型
        """
        myModule.roles.role.name = "villager"
        myModule.roles.role.side = myModule.roles.role.SIDE_VILLAGER
        myModule.roles.role.action = self.VillagerAction
        return
    

    def VillagerAction(self,player):
        return None
