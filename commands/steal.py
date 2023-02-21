import sqlite3
from random import randint
import math

with sqlite3.connect("economy.db") as db:
    cursor = db.cursor()

class info:
    name = "Steal from player"
    description = "Steals 20% of a players money"
    usage = "rob [@user]"

def run(discordID, target):
    if discordID != target:
        success = randint(1, 5)
        
        cursor.execute('''
    SELECT * FROM users
    WHERE discordID = ?
    ''', [discordID])

        own_money = cursor.fetchall()

        target_money = cursor.execute('''
    SELECT * FROM users
    WHERE discordID = ?
    ''', [target])

        target_money = cursor.fetchall()

        if own_money[0][4] != 1: 
            print(own_money[0][2], target_money[0][2])

            if success == 1:
                money_stolen = math.ceil(target_money[0][2]* 0.2)
                cursor.execute('''
        UPDATE users
        SET money = money + ?, last_rob = ?
        WHERE discordID = ?
        ''', [(money_stolen), (1), (discordID)])
                
                cursor.execute('''
        UPDATE users
        SET money = money - ?
        WHERE discordID = ?    
        ''', [(money_stolen), (target)])

                db.commit()

                return discordID + " has robbed " + target + " and has taken $" + str(int(money_stolen))
            
            else:
                return "You failed your robbery."
        else:
            return "You are on a cooldown."
    else:
        return "You can't rob yourself bozo."