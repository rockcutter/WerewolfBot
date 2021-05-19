from MyModule.RoleModule import role

class villager(role.role):
    """description of class"""

    def __init__(self):
        """
        コンストラクタ
        """
        self.name = "villager"
        self.side = role.SIDE_VILLAGER
        self.action = self.VillagerAction
        return    

    def VillagerAction(self,player):
        return None
