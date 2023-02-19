import discord

from random import randint

class info:
    name = "Gay test"
    description = "Tests someone for how gay they are"
    usage = "gay test [@user]"


async def run(user_ping, channel, args):
    if args[0] == "<@796834786580103179>":
        await channel.send("100%")
    elif args[0] == "<@1070730197302771792>":
        await channel.send("-1%")
    else:
        number = str(randint(0, 100))
        await channel.send(number + "% gay")