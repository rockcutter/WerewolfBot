class player(object):
    """description of class"""
    playerData = None
    role = None

    def __init__(self,playerObj):
        self.playerData = playerObj
        return
    
    def RegisterRole(self,roleObj):
        self.role = roleObj
        return

    def RoleNameStr(self):
        return self.role.name