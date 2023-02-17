import discord

import commands.question as question
import commands.howmanyburgers as burgers
import commands.gaytest as gaytest

import commands.economy.adduser as add_user
import commands.economy.crime as crime
import commands.economy.steal as steal_from_player
import commands.economy.viewmoney as view_money
import commands.economy.topten as topten
import commands.economy.buy as buy
import commands.economy.viewinventory as view_inventory
import commands.economy.give as give
import commands.economy.slots as slots

import commands.help as help

async def get_response(message: str, userID, channel) -> str:
    user_ping = "<@" + str(userID) + ">"
    
    p_message = message.lower()

    for item in question.questions:
        if item == p_message.split(" ", 1)[0]:
            return question.get_response()


    if p_message == "help":
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


    if " ".join(p_message.split(" ")[:3]) == "how many burgers":
        return burgers.get_burgers(p_message.split(" ")[:4][3])


    if " ".join(p_message.split(" ")[:2]) == "gay test":
        return gaytest.get_gayness(p_message.split(" ")[:3][2])

    if p_message == "what are you and joe doing tonight":
        return "https://media.tenor.com/rV8mpdXgZpAAAAAS/i-show-speed-speed.gif"


    if " ".join(p_message.split(" ")) == "create account":
        return add_user.add_user(user_ping)


    if " ".join(p_message.split(" ")) == "balance" or " ".join(p_message.split(" ")) == "bal":
        return view_money.view_money(user_ping)

    if " ".join(p_message.split(" ")) == "inventory":
        return view_inventory.view_inventory(user_ping)

    if " ".join(p_message.split(" ")[:2]) == "top ten" or " ".join(p_message.split(" ")[:2]) == "top 10":
        return topten.top_ten()

    if " ".join(p_message.split(" ")) == "crime":
        return crime.crime(user_ping)

    if " ".join(p_message.split(" ")) == "shop":
        embed=discord.Embed(title="The Flop Shop", description="Hello and welcome to the flop shop, take a look around.", color=0xff0000)
        embed.set_thumbnail(url="https://preview.redd.it/lstv0sesju991.jpg?auto=webp&s=5ff42783cbac81d0cd8a2f53445ceebc431cc4fb")
        embed.add_field(name="Weed (10kg)", value="$100", inline=False)
        embed.add_field(name="Phone", value="$500", inline=False)
        embed.add_field(name="Artifact", value="$50000", inline=False)
        embed.add_field(name="Sleepover", value="$5", inline=True)
        embed.set_footer(text="Check back next week for more items")
        await channel.send(embed=embed)


    if " ".join(p_message.split(" ")) == "blackmarket":
        embed=discord.Embed(title="The Black Market", description="What do you need?")
        embed.set_thumbnail(url="https://cdn.vox-cdn.com/thumbor/RrK_Jrhsrd3SfTKGGksueM-m-l8=/1400x1400/filters:format(jpeg)/cdn.vox-cdn.com/uploads/chorus_asset/file/9253051/Xur_Destiny_2_.jpg")
        embed.add_field(name="Booty Pic", value="$5000", inline=False)
        embed.add_field(name="Noah Pic", value="$1000", inline=False)
        embed.add_field(name="Joe Pic", value="$2500", inline=False)
        embed.add_field(name="Rexley Pic", value="$2500", inline=False)
        embed.set_footer(text="E.g 'bm purchase rexleypic'")
        await channel.send(embed=embed)

    if " ".join(p_message.split(" ")[:1]) == "buy":
        return buy.buy(user_ping, p_message.split(" ")[:2][1])

    if " ".join(p_message.split(" ")[:1]) == "rob":
        return steal_from_player.steal_from_player(user_ping, p_message.split(" ")[:2][1])

    if p_message == "slots":
        return slots.roll(user_ping)

    if " ".join(p_message.split(" ")) == "ping me":
        return user_ping

    if " ".join(p_message.split(" ")[:1]) == "give":
        return give.give_to_player(user_ping, p_message.split(" ")[1], p_message.split(" ")[2])