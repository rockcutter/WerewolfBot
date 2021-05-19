import discord
#Manager
from MyModule.ManagerModule import PlayerManager
from MyModule.ManagerModule import RoleManager
from MyModule.ManagerModule import GameManager
#role
from MyModule.RoleModule import villager
from MyModule.RoleModule import werewolf
#player
from MyModule.PlayerModule import player
#util
from MyModule.Utilities import UtilFunctions
#discord
from MyModule.DiscordControl import DiscordControl
#readenv
import readenv

#管理クラス
plmgr = PlayerManager.PlayerManager()
rolemgr = RoleManager.RoleManager()
gmmgr = GameManager.GameManager()

#discordコントロールクラス
discCtrl = DiscordControl.DiscordControl()

client = discord.Client()


#どうすんのこれ
import MyModule.gamemaster
gm = MyModule.gamemaster.gamemaster()



def main():
    #人狼ゲームの受付&ゲームが開始しているかどうか(人狼ゲームそのものの開始判定フラグ
    
    
    @client.event
    async def on_ready():
        print("ready")

    @client.event
    async def on_message(message):
        if(str(message.content)[0] != "!"):return

        if(message.content == "!werewolf"):
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

        if(gmmgr.CheckStatus() == GameManager.STATUS_ACCEPTSUPPORTCMD):
            await SupportCmd(message)
            return
        
    client.run(readenv.TOKEN)


async def ReceptionPhaseCmd(message):
    if(message.content == "!join" ):
        if(plmgr.IsPlayer(message.author)):
            return
        tempPlayerObj = MyModule.PlayerModule.player.player()
        tempPlayerObj.RegisterPlayerObj(message.author)
        tempPlayerObj.RegisterRole(None)
        plmgr.AppendPlayer(tempPlayerObj)
        await message.channel.send(str(message.author) + "の参加を受け付けました")        
        return

    if(message.content == "!set"):
        #phase識別が必要
        #ロール人数の決定
        for tempRoleObj in rolemgr.LoadAllRoleList():
            await SetRoleCount(tempRoleObj)
        await discCtrl.Say("役職数の登録が完了しました")

    if(message.content == "!start"):
        if(rolemgr.LoadVillageRoleCount() + rolemgr.LoadWolfRoleCount() <= 0):
            await discCtrl.Say("!set")
            return
        gmmgr.StartGame()
        await discCtrl.Say("!start")
        return
    return


async def SetRoleCount(roleObj):
    await discCtrl.Say(str(roleObj.name) + "の人数を設定してください")
    tempCount = await UtilFunctions.WaitforInteger(client)
    for i in range(tempCount):
        rolemgr.AppendRole(roleObj)
    return


async def InProgressPhaseCmd(message):
    if(message.content == "!start"):
        gmmgr.LimitCommand()

        a = rolemgr.LoadRandomizedRoleObjList()
        plmgr.ApplyRole(a)
        print(a)
        for tempPlCls in plmgr.LoadPlayerClassList():
            await tempPlCls.LoadPlayerObj().send("あなたの役職は" + tempPlCls.LoadRoleObj().RoleNameStr()+ "です")
            
        gm.Start()
        await discCtrl.Say("(なんか長いルール説明)")
        while(gm.GameInProgress()):
            #フェイズ初期化
            gm.TimePasses()
            gm.InitVotedList()

            #フェイズ分岐処理
            if(gm.GetDayPhase() == MyModule.gamemaster.DAYPHASE_NIGHTPHASE):
                #昨晩の結果発表処理
                await discCtrl.Say(str(gm.GetDay())+"日目 "+ "昼")
                await discCtrl.Say("昼になりました。誰が人狼なのかを話し合い、本日処刑する人を決めてもらいます。話し合いの後に処刑する人の投票を行います。")

                #vote処理が完成するまでbreak
                break

                while(gm.MemberCount() > gm.VotedCount()):
                    message = await client.wait_for("message")
                    if(not IsInt(message.content)):
                        continue
                    gm.Vote(message)

                await gm.Execution(message.guild)

            else:
                await discCtrl.Say(str(gm.GetDay())+"日目 "+ "夜")
                await discCtrl.Say("恐ろしい夜の時間がやってきました。役職持ちのプレイヤーはDMにてアクションを行ってください")
                                
                #人狼アクション
                
                #占い師アクション

            
    if(message.content == "!list"):
        for i in range(len(gm.GetMemberList())):
            await channel.send(str(i) + ": " + str(gm.GetMemberList()[i].playerData))
    return

async def SupportCmd(message):
    if(message.content == "!list"):
        for i in range(len(plmgr.LoadPlayerClassList())):
            await discCtrl.Say(str(i) +": " + str(plmgr.LoadPlayerClassList()[i].LoadPlayerObj()))
    return



if __name__ == "__main__":
    main()

