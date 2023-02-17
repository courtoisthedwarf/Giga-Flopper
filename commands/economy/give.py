import sqlite3
from random import randint
import math

with sqlite3.connect("economy.db") as db:
    cursor = db.cursor()

def give_to_player(discordID, target, amount):
    if discordID != target:
        cursor.execute('''
SELECT * FROM users
WHERE discordID =?
''', [discordID])
        
        user = cursor.fetchall()

        if user[0][2] <= 0:
            return "You don't have enough money for that."
        else:
            
            
            cursor.execute('''
    UPDATE users
    SET money = money - ?
    WHERE discordID = ?
    ''', [(amount), (discordID)])
            
            cursor.execute('''
    UPDATE users
    SET money = money + ?
    WHERE discordID = ?    
    ''', [(amount), (target)])

            db.commit()

            return discordID + " has given " + target + " $" + str(int(amount))
        