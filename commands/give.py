import sqlite3
from random import randint

with sqlite3.connect("Giga-Flopper\economy.db") as db:
    cursor = db.cursor()

async def run(user_ping, channel, args):
    if user_ping != args[0]:
        cursor.execute('''
SELECT * FROM users
WHERE discordID =?
''', [user_ping])
        
        user = cursor.fetchall()

        if user[0][2] <= 0:
            return "You don't have enough money for that."
        else:
            
            
            cursor.execute('''
    UPDATE users
    SET money = money - ?
    WHERE discordID = ?
    ''', [(args[1]), (user_ping)])
            
            cursor.execute('''
    UPDATE users
    SET money = money + ?
    WHERE discordID = ?    
    ''', [(args[1]), (args[0])])

            db.commit()

            await channel.send(user_ping + " has given " + args[0] + " $" + str(int(args[1])))
        