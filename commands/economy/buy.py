import sqlite3

with sqlite3.connect("economy.db") as db:
    cursor = db.cursor()

items = [
    ("weed", 100),
    ("phone", 500),
    ("artifact", 50000),
    ("sleepover", 5) 
]
def buy(discordID, request):
    cursor.execute('''
SELECT * FROM users
WHERE discordID = ?;
''', [discordID])
    
    user = cursor.fetchall()
    
    for item in items:
        if item[0] == request.lower():
            if item[1] <= user[0][2]:
                new_inventory = str(user[0][3]) + ":" + str(request)
                
                update = '''
UPDATE users
SET items = ?, money = money - ?
WHERE discordID = ?;
''' 

                cursor.execute(update, [(new_inventory), (item[1]), (discordID)])
                db.commit()

                return "Transaction completed for " + request + ": - $" + str(item[1])
            elif user[2] < item[1]:
                return "You don't have enough money to buy that lmao."
        else:
            continue
