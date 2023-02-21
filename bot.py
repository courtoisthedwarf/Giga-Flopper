import discord
import commandhandler

def run_bot(TOKEN):
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents = intents)

    @client.event
    async def on_ready():
        print(f'{client.user} is online')

    
    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        username = str(message.author)
        userID = int(message.author.id)
        user_message = str(message.content)
        channel = str(message.channel)

        print(f'{username} said: "{user_message}" ({channel})')

        if user_message[:6].lower() == "floppa" or user_message[:7].lower() == "flopper" or user_message[:4].lower() == "flop":
            user_message = user_message.split(" ", 1)
            await commandhandler.handle(user_message[1], userID, message.channel)

    
    
    client.run(TOKEN)
