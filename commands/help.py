import discord

class info:
    name = "Help"
    description = "List of commands"
    usage = "help"

async def test_embed(channel):
    embed = discord.Embed(title="Help menu", description="list of commands")
    embed.add_field(name="command", value="description", inline=True)
    embed.add_field(name="other command", value="other description", inline=True)
    embed.add_field(name="etc etc", value="(etc etc)", inline=True)
    embed.add_field(name="wowee", value="im mr meeseks look at me", inline=True)
    embed.set_footer(text="need more help? dm me @courtoisthedwarf#6837")

    await channel.send(embed = embed)