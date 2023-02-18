import discord
import commandhandler

async def send_message(message, userID, channel, user_message, is_private):
    try:
        response = await commandhandler.get_response(user_message, userID, channel)
        await message.author.send(response) if is_private else await message.channel.send(response)
    
    except Exception as error:
        print(error)

    

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
            await send_message(message, userID, message.channel, user_message[1], is_private = False)
        elif user_message[:2].lower() == "bm":
            await send_message(message, userID, message.channel, user_message[1], is_private = True)

    
    
    client.run(TOKEN)
