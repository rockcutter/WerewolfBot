import discord

from myModule import game
import readenv

client = discord.Client()

def main():
    gm = game.game()

    

    @client.event
    async def on_ready():
        print("ready")

    @client.event
    async def on_message(message):
        if(message.content == "!join"):
            if(gm.AddMember(message.author)):
                await message.channel.send(str(message.author) + "の参加を受け付けました")
            return


    client.run(readenv.TOKEN)

if __name__ == "__main__":
    main()