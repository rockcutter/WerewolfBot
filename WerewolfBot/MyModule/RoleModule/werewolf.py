import MyModule.roles.role
import readenv

class werewolf(myModule.roles.role.role):
    """人狼ロール"""
    guild = None

    def __init__(self,argGuild):
        """
        コンストラクタ
        Args:
            argGuild: データ型
        """
        myModule.roles.role.name = "werewolf"
        myModule.roles.role.side = myModule.roles.role.SIDE_WEREWOLF
        myModule.roles.role.action = self.WerewolfAction
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