from MyModule.RoleModule import role
import readenv

class werewolf(role.role):
    """人狼ロール"""
    guild = None

    def __init__(self,argGuild):
        """
        コンストラクタ
        Args:
            argGuild: データ型
        """
        role.role.name = "werewolf"
        role.role.side = role.SIDE_WEREWOLF
        role.role.action = self.WerewolfAction
        self.guild = argGuild
        return
    

    def WerewolfAction(self,player):
        """
        人狼アクションを行う キル対象のプレイヤー情報をplayerに代入
        Args:
            player:Member型
        """    
        self.AddRole(player)
        return 

    async def AddRole(self,player):
        """
        killedロールを付与する
        """
        killedRole = self.guild.get_role(readenv.KILLEDID)
        await player.add_roles(killedRole)
        return