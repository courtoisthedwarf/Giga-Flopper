from random import randint
import sqlite3

with sqlite3.connect("economy.db") as db:
    cursor = db.cursor()


def roll(discordID):
    fruit = [
        "🍇", 
        "🍒",
        "🍍",
        "🥝",
        "🍊",
        "🍋",
        "🍉",
        "🥭"
    ]

    slots = [randint(0, len(fruit) - 1), randint(0, len(fruit) - 1), randint(0, len(fruit) - 1)]

    rolled_fruits = ""
    rolled_amount = ""

    for slot in slots:
        rolled_fruits = rolled_fruits + fruit[slot]
        rolled_amount = rolled_amount + str(slot)

    earned = int(rolled_amount)

    cursor.execute('''
UPDATE users
SET money = money + ?
WHERE discordID = ?;
''', [(earned - 500), (discordID)])

    db.commit()

    return rolled_fruits + "\n Congratulations, you won $" +  rolled_amount.lstrip("0")