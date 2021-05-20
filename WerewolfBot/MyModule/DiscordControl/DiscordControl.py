class DiscordControl(object):
    """discord関連の機能を持つクラス"""

    guild = None
    channel = None
    client = None

    def RegisterGuild(self,argGuild):
        """人狼が開催されるGuildを登録する関数"""
        self.guild = argGuild
        return

    def RegisterChannel(self,argChannel):
        """人狼が開催されるchannelを登録する関数"""
        self.channel = argChannel
        return

    def RegisterClient(self,argClient):
        self.client = argClient
        return

    async def AddRole(self,playerObj,roleID):
        """ロールを付与する"""
        role = self.guild.get_role(roleID)
        await playerObj.add_roles(role)
        return

    async def Say(self,message):
        await self.channel.send(message)
        return