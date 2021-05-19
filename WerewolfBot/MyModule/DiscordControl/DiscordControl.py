class DiscordControl(object):
    """discord関連の機能を持つ関数"""

    guild = None
    channel = None

    def RegisterGuild(self,argGuild):
        """人狼が開催されるGuildを登録する関数"""
        self.guild = argGuild
        return

    def RegisterChannel(self,argChannel):
        self.channel = argChannell
        return