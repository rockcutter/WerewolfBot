import discord
#Manager
from MyModule.ManagerModule import PlayerManager
from MyModule.ManagerModule import RoleManager
from MyModule.ManagerModule import GameManager
from MyModule.ManagerModule import VoteManager
#role
from MyModule.RoleModule import villager
from MyModule.RoleModule import werewolf
#player
from MyModule.PlayerModule import player
#util
from MyModule.Utilities import UtilFunctions
from MyModule.Utilities import cmdlist
#discord
from MyModule.DiscordControl import DiscordControl
#readenv
import readenv

#管理クラス
plmgr = PlayerManager.PlayerManager()
rolemgr = RoleManager.RoleManager()
gmmgr = GameManager.GameManager()
votemgr = VoteManager.VoteManager()
#discordコントロールクラス
discCtrl = DiscordControl.DiscordControl()

client = discord.Client()

def main():
    #人狼ゲームの受付&ゲームが開始しているかどうか(人狼ゲームそのものの開始判定フラグ
    
    
    @client.event
    async def on_ready():
        print("ready")

    @client.event
    async def on_message(message):
        if(str(message.content)[0] != "!"):return

        if(message.content == cmdlist.ACTIVATION):
            discCtrl.RegisterChannel(message.channel)
            discCtrl.RegisterGuild(message.guild)
            gmmgr.ActivateGame()
            await discCtrl.Say("Werewolf bot was activated!!")
            return

        await SupportCmd(message)

        #Phase分岐
        if(gmmgr.CheckStatus() == GameManager.STATUS_NOTACTIVATED):
            return

        if(gmmgr.CheckStatus() == GameManager.STATUS_RECEPTION):
            await ReceptionPhaseCmd(message)
            return

        if(gmmgr.CheckStatus() == GameManager.STATUS_INPROGRESS):
            await InProgressPhaseCmd(message)
            return
        
    client.run(readenv.TOKEN)


async def ReceptionPhaseCmd(message):
    if(message.content == cmdlist.JOIN ):
        if(plmgr.IsPlayer(message.author)):
            return
        tempPlayerObj = player.player()
        tempPlayerObj.RegisterPlayerObj(message.author)
        tempPlayerObj.RegisterRole(None)
        plmgr.AppendPlayer(tempPlayerObj)
        await message.channel.send(str(message.author) + "の参加を受け付けました")        
        return

    if(message.content == cmdlist.SETROLE):
        await discCtrl.Say("人数 < 役数だと役欠けが発生します")
        for tempRoleObj in rolemgr.LoadAllRoleList():
            await SetRoleCount(tempRoleObj)
        await discCtrl.Say("役職数の登録が完了しました")

    if(message.content == cmdlist.START):
        #start時エラー処理
        if(rolemgr.LoadRoleCount() <= 0):
            await discCtrl.Say(cmdlist.SETROLE)
            return
        if(len(plmgr.LoadPlayerClassList()) == 0):
            await discCtrl.Say("参加者が0人です")
            return 
        if(len(plmgr.LoadPlayerClassList()) > rolemgr.LoadRoleCount()):
            await discCtrl.Say("参加者数 > 役職数 です")
            return

        gmmgr.StartGame()
        await discCtrl.Say(cmdlist.START)
        return
    return


async def SetRoleCount(roleObj):
    await discCtrl.Say(str(roleObj.name) + "の人数を設定してください")
    tempCount = await UtilFunctions.WaitforInteger(client)
    for i in range(tempCount):
        rolemgr.AppendRole(roleObj)
    return


async def InProgressPhaseCmd(message):
    if(message.content == cmdlist.START):
        gmmgr.LimitCommand()

        a = rolemgr.LoadRandomizedRoleObjList()
        plmgr.ApplyRole(a)
        print(a)
        #DM処理
        for tempPlCls in plmgr.LoadPlayerClassList():
            await tempPlCls.LoadPlayerObj().send("あなたの役職は" + tempPlCls.LoadRoleObj().RoleNameStr()+ "です")
            print("あなたの役職は" + tempPlCls.LoadRoleObj().RoleNameStr()+ "です")
            
        await discCtrl.Say("(なんか長いルール説明)")
        while(True):
            #フェイズ初期化
            gmmgr.TimePasses()
            votemgr.ManuInit()


            #フェイズ分岐処理
            if(gmmgr.GetDayPhase() == 0b00000000):
                #昨晩の結果発表処理
                await discCtrl.Say(str(gmmgr.GetDay())+"日目 "+ "昼")
                await discCtrl.Say("昼になりました。誰が人狼なのかを話し合い、本日処刑する人を決めてもらいます。話し合いの後に処刑する人の投票を行います。")
                
                #投票先リストを表示する
                await discCtrl.Say(cmdlist.SHOWLIST)
                #ループ
                while(votemgr.LoadVoteCount() < plmgr.LoadPlayerCount()):
                    message = await client.wait_for("message")
                    splitedCmd = message.content.split()
                    if(splitedCmd[0] == cmdlist.VOTE and len(splitedCmd) > 1):
                        
                        votemgr.Vote(message.author, splitedCmd[1])

                print(votemgr.LoadMostVote())

                #処刑
                for playerNum in votemgr.LoadMostVote():
                    await discCtrl.AddRole(plmgr.LoadPlayerClassList()[int(playerNum)].playerObj,readenv.EXECUTEDID)

            else:
                await discCtrl.Say(str(gmmgr.GetDay())+"日目 "+ "夜")
                await discCtrl.Say("恐ろしい夜の時間がやってきました。役職持ちのプレイヤーはDMにてアクションを行ってください")
                #人狼アクション
                while(True):
                    message = await client.wait_for("message")
                    splitedCmd = message.content.split()
                    if(splitedCmd[0] == cmdlist.WEREWOLF_KILL and len(splitedCmd) > 1 and plmgr.LoadMatchedPlayerClass(message.author).LoadRoleObj().RoleNameStr() == "werewolf"):
                        await discCtrl.AddRole(plmgr.LoadPlayerClassList()[int(splitedCmd[1])].LoadPlayerObj(), readenv.KILLEDID)
                    break

    return

async def SupportCmd(message):
    if(message.content == cmdlist.SHOWLIST):
        for i in range(plmgr.LoadPlayerCount()):
            await message.channel.send(str(i) +": " + str(plmgr.LoadPlayerClassList()[i].LoadPlayerObj()))
    return



if __name__ == "__main__":
    main()

