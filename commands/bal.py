import sqlite3

with sqlite3.connect("economy.db") as db:
    cursor = db.cursor()

class info:
    name = "View money"
    description = "Views your current balance"
    usage = "bal"

async def run(user_ping, channel, args):
    cursor.execute('''
SELECT * FROM users
WHERE discordID = ?;
''', [user_ping])
    
    await channel.send("You have $" + f'{cursor.fetchall()[0][2]:,}')
