import sqlite3
from nltk.probability import FreqDist

with sqlite3.connect("economy.db") as db:
    cursor = db.cursor()

class info:
    name = "View backpack"
    description = "Views your items"
    usage = "inventory"

def view_inventory(discordID):
    cursor.execute('''
SELECT * FROM users
WHERE discordID = ?;
''', [discordID])
    
    backpack = cursor.fetchall()[0][3]
    items = backpack.split(":")

    frequency = {}

    for item in items:
        if item in frequency:
            frequency[item] += 1
        else:
            frequency[item] = 1



    return str(frequency)