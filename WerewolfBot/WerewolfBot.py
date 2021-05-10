import discord

import myModule.werewolf
import myModule.game
import readenv

client = discord.Client()

def main():
    gm = myModule.game.game()

    

    @client.event
    async def on_ready():
        print("ready")

    @client.event
    async def on_message(message):
        if(str(message.content)[0] == "!"):return

        if(not gm.GameInProgress()):
            await ReceptionPahseCmd(message)
            return

        


        
    client.run(readenv.TOKEN)


    async def ReceptionPhaseCmd(message):
        if(message.content == "!join" ):
            if(gm.AddMember(message.author)):
                await message.channel.send(str(message.author) + "の参加を受け付けました")
            return

        if(message.content == "!start"):
            gm.Start()
            return


if __name__ == "__main__":
    main()

