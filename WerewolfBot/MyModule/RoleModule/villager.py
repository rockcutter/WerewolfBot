from MyModule.RoleModule import role

class villager(role.role):
    """description of class"""

    def __init__(self):
        """
        コンストラクタ
        """
        role.role.name = "villager"
        role.role.side = role.SIDE_VILLAGER
        role.role.action = self.VillagerAction
        return    

    def VillagerAction(self,player):
        return None
