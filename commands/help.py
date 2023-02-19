import discord

class info:
    name = "Help"
    description = "List of commands"
    usage = "help"

async def run(user_ping, channel, args):
    embed=discord.Embed(title="Help Menu", color=0xff0000)
    embed.set_thumbnail(url="https://preview.redd.it/g8jksihn5dr61.png?auto=webp&s=00243fd080b8f9a83878e56692da969ab6b9445b")
    embed.add_field(name="help", value="Returns a list of my commands", inline=False)
    embed.add_field(name="gay test [@user]", value="Tests for someone's level of gayness", inline=False)
    embed.add_field(name="how many burgers [@user]", value="Returns someone's burger count", inline=False)
    embed.add_field(name="create account", value="Creates an account for the economy", inline=False)
    embed.add_field(name="crime", value="Commit a crime for money", inline=False)
    embed.add_field(name="rob [@user]", value="Attempt to steal 20% of a player's money", inline=False)
    embed.add_field(name="balance [@user]", value="See your balance", inline=False)
    embed.add_field(name="top ten", value="Returns top ten richest users", inline=False)
    embed.add_field(name="slots", value="Play slots, costs $500", inline=False)
    embed.add_field(name="inventory", value="View your inventory", inline=False)
    embed.add_field(name="give [@user]", value="Give money to another player", inline=False)
    embed.add_field(name="buy [item]", value="Buy an item", inline=False)
    embed.add_field(name="shop", value="View current shop", inline=False)

    await channel.send(embed = embed)