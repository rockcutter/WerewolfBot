SIDE_VILLAGER = 0
SIDE_WEREWOLF = 0

class role(object):
    """役職基底クラス"""
    name = None
    player = None
    action = None
    side = None

    def Action():
        """
        設定されたアクションを行う
        Returns:
            actionがNoneだった場合Falseを返す
        """
        if(action != None):
            return action()
        return False

    