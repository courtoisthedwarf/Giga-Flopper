import sqlite3

with sqlite3.connect("economy.db") as db:
    cursor = db.cursor()

class info:
    name = "View money"
    description = "Views your current balance"
    usage = "balance"

def view_money(discordID):
    cursor.execute('''
SELECT * FROM users
WHERE discordID = ?;
''', [discordID])
    
    return "You have $" + f'{cursor.fetchall()[0][2]:,}'
