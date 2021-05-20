class VoteManager(object):
    """投票を管理するクラス 別名選挙管理委員会"""
    votedDict = {}
    votedCount = 0
    votedPlayerObjList = []

    def __init__(self):
        self.votedDict = {}
        self.votedCount = 0
        self.votedPlayerObjList = []
        return

    

    def Vote(self,votedPlayerObj, voteTarget):
        if(votedPlayerObj in self.votedPlayerObjList):
            return

        if(voteTarget not in self.votedDict):
            self.votedDict[voteTarget] = 1
        else:
            self.votedDict[voteTarget] += 1
        self.votedCount += 1
        self.votedPlayerObjList.append(votedPlayerObj)
        return

    def LoadVoteCount(self):
        return self.votedCount

    def LoadVoteRankingDict(self):
        return sorted(self.votedDict.items,key = lambda x:x[1])

    def LoadMostVote(self):
        maxKeyList = []
        maxVoteCount = -1

        for k,i in self.votedDict.items():
            if(maxVoteCount < i):
                maxKeyList = []
                maxKeyList.append(k)
                maxVoteCount = i
                continue
            if(maxVoteCount == i):
                maxKeyList.append(k)
                continue
        return maxKeyList
