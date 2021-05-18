import myModule.game
import random
import readenv

DAYPHASE_NOONPHASE = 0b00000001
DAYPHASE_NIGHTPHASE = 0b00000000

class gamemaster(myModule.game.game):
    time = None
    roleList = []
    votedList = []
    votedCount = 0

    def __init__(self):
        self.time= 0b00000001 #最下位ビットが1で夜 初期化は0日目夜
        return

    def RegisterRole(self):
        #ロールリストのシャッフル
        random.shuffle(self.roleList)
        #ロールをプレイヤーに付与
        print(self.roleList)
        for mem in myModule.game.game.member:
            mem.RegisterRole(self.roleList.pop(0))
        return

    def RoleList(self):
        return self.roleList

    def TimePasses(self):
        self.time += 1
        return

    def GetDay(self):
        return self.time >> 1

    def GetDayPhase(self):
        return self.time & 0b00000001
    
    def Vote(self,message):
        if(0 <= int(message.content) and int(message.content) < len(myModule.game.game.member)):
            self.votedList[int(message.content)] += 1
            self.votedCount += 1
            return True
        return False

    def VotedCount(self):
        return self.votedCount
    

    def InitVotedList(self):
        self.votedList = [0] * len(myModule.game.game.member)
        self.votedCount = 0
        return 

    def AddRoleList(self,roleData,count):
        for buf in range(count):
            self.roleList.append(roleData)
        return

    async def AddRole(self,player,guild):
        executedRole = guild.get_role(readenv.EXECUTEDID)
        await player.add_roles(executedRole)
        return

    async def Execution(self,guild):
        #処刑する関数
        for i in range(len(self.votedList)):
            if(self.votedList[i] == max(self.votedList)):
                
                await self.AddRole(myModule.game.game.member[i].playerData,guild)
                return True
        return False
