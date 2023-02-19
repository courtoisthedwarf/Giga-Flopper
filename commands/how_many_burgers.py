from random import randint

class info:
    name = "How many burgers"
    description = "Returns their burger count"
    usage = "how many burgers [@user]"

async def run(user_ping, channel, args):
    if args[0] == "<@799198085632753674>":
        await channel.send("ALL OF EM")
    else:
        await channel.send(randint(0, 20))