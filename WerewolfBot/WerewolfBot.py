import discord

client = discord.Client()

def main():


    @client.event
    async def on_ready():
        print("ready")

    @client.event
    async def on_message(message):
        pass

    client.run(TOKEN)

if __name__ == "__main__":
    main()