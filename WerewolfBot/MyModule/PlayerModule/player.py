class player(object):
    """description of class"""
    playerObj = None
    roleObj = None
    
    def __init__(self):
        playerObj = None
        roleObj = None
        return

    def RegisterPlayerObj(self,argObj):
        self.playerObj = argObj
        return

    def RegisterRole(self,argObj):
        self.roleObj = argObj
        return

    def LoadPlayerObj(self):
        return self.playerObj