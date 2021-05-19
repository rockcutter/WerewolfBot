class DiscordControl(object):
    """discord関連の機能を持つ関数"""

    guild = None
    channel = None

    def RegisterGuild(self,argGuild):
        """人狼が開催されるGuildを登録する関数"""
        self.guild = argGuild
        return

    def RegisterChannel(self,argChannel):
        """人狼が開催されるchannelを登録する関数"""
        self.channel = argChannell
        return

    async def AddRole(self,playerObj,roleID):
        """ロールを付与する"""
        role = self.guild.get_role(roleID)
        await playerObj.add_roles(role)
        return

    async def Say(self,message):
        await channel.send(message)
        return