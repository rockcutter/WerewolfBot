SIDE_VILLAGER = 0
SIDE_WEREWOLF = 1

class role(object):
    """役職基底クラス"""
    name = None
    action = None
    side = None

    def Action(self,arg):
        """
        設定されたアクションを行う
        Args: 
            arg: アクションに必要な変数
        Returns:
            actionがNoneだった場合Falseを返す
        """
        if(action != None):
            return action(arg)
        return False

    def RoleNameStr(self):
        return name;
    