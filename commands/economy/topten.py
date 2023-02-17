import sqlite3

with sqlite3.connect("economy.db") as db:
    cursor = db.cursor()

class info:
    name = "View money"
    description = "Views your current balance"
    usage = "balance"

def top_ten():
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
            results = results + str(count) + ". " + str(player[1]) + ": $" + str(player[2]) + "\n"

    return results