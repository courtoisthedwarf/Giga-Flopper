import sqlite3

with sqlite3.connect("Giga-Flopper\economy.db") as db:
    cursor = db.cursor()

class info:
    name = "View money"
    description = "Views your current balance"
    usage = "balance"

async def run(user_ping, channel, args):
    cursor.execute('''
SELECT * FROM users
WHERE discordID = ?;
''', [user_ping])
    
    await channel.send("You have $" + f'{cursor.fetchall()[0][2]:,}')
