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
            gm.AddMember(message.author)
    client.run(readenv.TOKEN)

if __name__ == "__main__":
    main()