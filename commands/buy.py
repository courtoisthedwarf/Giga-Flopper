import sqlite3

with sqlite3.connect("Giga-Flopper\economy.db") as db:
    cursor = db.cursor()

class Info:
    name = "Buy"
    description = "Purchase an item from the shop"
    usage = "buy [item]"    


items = [
    ("weed", 100),
    ("phone", 500),
    ("artifact", 50000),
    ("sleepover", 5) 
]

async def run(user_ping, channel, args):
    cursor.execute('''
SELECT * FROM users
WHERE discordID = ?;
''', [user_ping])
    
    user = cursor.fetchall()
    
    for item in items:
        if item[0] == args[0].lower():
            if item[1] <= user[0][2]:
                new_inventory = str(user[0][3]) + ":" + str(args[0])
                
                update = '''
UPDATE users
SET items = ?, money = money - ?
WHERE discordID = ?;
''' 

                cursor.execute(update, [(new_inventory), (item[1]), (user_ping)])
                db.commit()

                await channel.send("Transaction completed for " + args[0] + ": - $" + str(item[1]))
            elif user[2] < item[1]:
                await channel.send("You don't have enough money to buy that lmao.")
        else:
            continue
