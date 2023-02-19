import sqlite3
from nltk.probability import FreqDist

with sqlite3.connect("Giga-Flopper\economy.db") as db:
    cursor = db.cursor()

class info:
    name = "View backpack"
    description = "Views your items"
    usage = "inventory"

async def run(user_ping, channel, args):
    cursor.execute('''
SELECT * FROM users
WHERE discordID = ?;
''', [user_ping])
    
    backpack = cursor.fetchall()[0][3]
    items = backpack.split(":")

    frequency = {}

    for item in items:
        if item in frequency:
            frequency[item] += 1
        else:
            frequency[item] = 1



    await channel.send(str(frequency))