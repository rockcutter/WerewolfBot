import discord

from MyModule.ManagerModule import PlayerManager
from MyModule.ManagerModule import RoleManager

import MyModule.PlayerModule.player
import MyModule.RoleModule.werewolf
import MyModule.RoleModule.villager
import MyModule.gamemaster

import MyModule.PlayerModule.player
import readenv


client = discord.Client()
gm = MyModule.gamemaster.gamemaster()

#管理クラス
plmgr = PlayerManager()
rlmgr = RoleManager()

def main():
     

    @client.event
    async def on_ready():
        print("ready")

    @client.event
    async def on_message(message):
        if(str(message.content)[0] != "!"):return

        #受付状態のコマンド処理
        if(not gm.GameInProgress()):
            await ReceptionPhaseCmd(message)
            return

        if(gm.GameInProgress()):
            await InProgressPhaseCmd(message)
            return


        
    client.run(readenv.TOKEN)


async def ReceptionPhaseCmd(message):
    if(message.content == "!join" ):
        tempPlayerObj = MyModule.PlayerModule.player.player()
        tempPlayerObj.RegisterPlayerObj(message.author)
        tempPlayerObj.RegisterRole(None)
        plmgr.AppendPlayer()
        return

    if(message.content == "!set"):
        #phase識別が必要
        #ロール人数の決定
        await message.channel.send("村人の人数を設定してください")
        roleCountStr = message #初期化のため
        while(not IsInt(roleCountStr.content)):
            roleCountStr = await client.wait_for("message")
        #村人ロールの登録
        roleObjBuf = MyModule.roles.villager.villager()
        gm.AddRoleList(roleObjBuf,int(roleCountStr.content))
        
        await message.channel.send("人狼の人数を設定してください")
        roleCountStr = message #初期化のため
        while(not IsInt(roleCountStr.content)):
            roleCountStr = await client.wait_for("message")
            print("test")
        #村人ロールの登録
        roleObjBuf = MyModule.roles.werewolf.werewolf(message.guild)
        gm.AddRoleList(roleObjBuf,int(roleCountStr.content))

    if(message.content == "!start"):
        if(len(gm.RoleList()) == 0):
            await message.channel.send("!set")
            return
        gm.Start()
        await message.channel.send("!start")
    return


async def InProgressPhaseCmd(message):
    channel = message.channel
    if(message.content == "!start"):
        
        gm.RegisterRole()
        for mem in gm.member:
            await mem.playerData.send("あなたの役職は" + mem.role.RoleNameStr()+ "です")
            
        gm.Start()
        await channel.send("(なんか長いルール説明)")
        while(gm.GameInProgress()):
            #フェイズ初期化
            gm.TimePasses()
            gm.InitVotedList()

            #フェイズ分岐処理
            if(gm.GetDayPhase() == MyModule.gamemaster.DAYPHASE_NIGHTPHASE):
                #昨晩の結果発表処理
                await channel.send(str(gm.GetDay())+"日目 "+ "昼")
                await channel.send("昼になりました。誰が人狼なのかを話し合い、本日処刑する人を決めてもらいます。話し合いの後に処刑する人の投票を行います。")

                

                while(gm.MemberCount() > gm.VotedCount()):
                    message = await client.wait_for("message")
                    if(not IsInt(message.content)):
                        continue
                    gm.Vote(message)

                await gm.Execution(message.guild)

            else:
                await channel.send(str(gm.GetDay())+"日目 "+ "夜")
                await channel.send("恐ろしい夜の時間がやってきました。役職持ちのプレイヤーはDMにてアクションを行ってください")
                                
                #人狼アクション
                
                #占い師アクション




            #先の処理を追加するまでbreak
            
    if(message.content == "!list"):
        for i in range(len(gm.GetMemberList())):
            await channel.send(str(i) + ": " + str(gm.GetMemberList()[i].playerData))
    return

def IsInt(val):
    try:
        int(val)
    except ValueError:
        return False
    else:
        return True



if __name__ == "__main__":
    main()

