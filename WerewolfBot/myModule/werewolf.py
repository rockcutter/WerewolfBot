import myModule.role
import readenv

class werewolf(myModule.role.role):
    """人狼ロール"""
       

    def __init__(self,argGuild):
        """
        コンストラクタ
        Args:
            guild: データ型
        """
        myModule.role.name = "werewolf"
        myModule.role.player = None
        myModule.role.side = myModule.role.SIDE_WEREWOLF
        myModule.role.action = self.WerewolfAction
        myModule.role.guild = argGuild
        
        return
    
    def WerewolfAction(self,player):
        """
        人狼アクションを行う キル対象のプレイヤー情報をplayerに代入
        Args:
            player:Member型
        """         
        return self.AddRole(player)


    async def AddRole(self,player):
        """
        killedロールを付与する
        """
        killedRole = myModule.role.guild.get_role(readenv.KILLEDID)
        await player.add_roles(killedRole)
        return