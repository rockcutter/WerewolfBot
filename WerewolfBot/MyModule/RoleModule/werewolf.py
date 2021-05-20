from MyModule.RoleModule import role
import readenv

class werewolf(role.role):
    """人狼ロール"""

    def __init__(self):
        """
        コンストラクタ
        Args:
            argGuild: データ型
        """
        self.name = "werewolf"
        self.side = role.SIDE_WEREWOLF
        self.action = self.WerewolfAction
        return
    

    def WerewolfAction(self,arg1 = None, arg2 = None,arg3 = None):
        """
        人狼アクションを行う キル対象のプレイヤー情報をplayerに代入
        Args:
            player:Member型
        """    


        return 