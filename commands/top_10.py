import sqlite3

with sqlite3.connect("economy.db") as db:
    cursor = db.cursor()

class info:
    name = "Top 10"
    description = "Views top 10 players"
    usage = "top 10"

async def run(user_ping, channel, args):
    cursor.execute('''
SELECT * FROM users
ORDER BY money DESC
''')
    
    players = cursor.fetchall()

    results = ""
    count = 0

    for player in players:
        if count != 10:  
            count = count + 1
            results = results + str(count) + ". " + str(player[1]) + ": $" + f'{int(player[2]):,}' + "\n"

    await channel.send(results)