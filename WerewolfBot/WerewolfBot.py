import discord

import myModule.roles.werewolf
import myModule.roles.villager
import myModule.gamemaster
import myModule.player
import readenv


client = discord.Client()
gm = myModule.gamemaster.gamemaster()

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

        if(gm.GameInProgres()):

            return


        
    client.run(readenv.TOKEN)


async def ReceptionPhaseCmd(message):
    if(message.content == "!join" ):
        playerData = myModule.player.player(message.author)
        if(gm.AddMember(playerData)):
            await message.channel.send(str(message.author) + "の参加を受け付けました")
        return

    if(message.content == "!setting"):
        #phase識別が必要
        #ロール人数の決定
        await message.channel.send("村人の人数を設定してください")
        roleCountStr = message #初期化のため
        while(not IsInt(roleCountStr.content)):
            roleCountStr = await client.wait_for("message")
        #村人ロールの登録
        roleObjBuf = myModule.roles.villager.villager()
        gm.AddRoleList(roleObjBuf,int(roleCountStr.content))
        
        await message.channel.send("人狼の人数を設定してください")
        roleCountStr = message #初期化のため
        while(not IsInt(roleCountStr.content)):
            roleCountStr = await client.wait_for("message")
            print("test")
        #村人ロールの登録
        roleObjBuf = myModule.roles.werewolf.werewolf(message.guild)
        gm.AddRoleList(roleObjBuf,int(roleCountStr.content))

    if(message.content == "!start"):
        channel = message.channel
        gm.RegisterRole()
        for mem in gm.member:
            await mem.playerData.send("あなたの役職は" + mem.role.RoleNameStr()+ "です")

        gm.Start()
        await channel.send("(なんか長いルール説明)")
        while(gm.GameInProgress()):
            gm.TimePasses()
            if(gm.GetDayPhase() == myModule.gamemaster.DAYPHASE_NIGHTPHASE):
                await channel.send(str(gm.GetDay())+"日目 "+ "昼")
                await channel.send("昼になりました。誰が人狼なのかを話し合い、本日処刑する人を決めてもらいます。話し合いの後に処刑する人の投票を行います。")





            else:
                await channel.send(str(gm.GetDay())+"日目 "+ "夜")
                await channel.send("恐ろしい夜の時間がやってきました。役職持ちのプレイヤーはDMにてアクションを行ってください")





            #先の処理を追加するまでbreak
            break
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

