import sqlite3
from random import randint

with sqlite3.connect("economy.db") as db:
    cursor = db.cursor()

class info:
    name = "Crime"
    description = "Commit a crime for money"
    usage = "crime"

async def run(user_ping, channel, args):
    blessed = False
    earned = 0

    cursor.execute('''
SELECT * FROM users
WHERE discordID = ?    
''', [user_ping])

    user = cursor.fetchall()

    for item in user[0][3].split(":"):
        if item == "artifact":
            if randint(0,100) == 1 or user_ping == "<@660156765689872395>":
                blessed = True
                earned = randint(1000, 50000)
            else:
                earned = randint(-20, 180)
        else:
            earned = randint(-20, 180)
            

    crimes = [
        "You committed an armed robbery",
        "You cashed out on an insurance scam",
        "You stole from an old aged pensioner",
        "You burgled a mansion",
        "You successfully created a pyramid scheme",
        "You sold cat nip"
    ]


    failed_crimes = [
        "You failed an armed robbery",
        "Your insurance scam failed",
        "You attempted to steal from an old aged pensioner but they dropped you,",
        "You were caught burgling a mansion",
        "You attempted to make a pyramid scheme but it never took off",
        "You got scammed out of your cat nip"
]


    edit = '''
UPDATE users
SET money = money + ?
WHERE discordID = ?;    
'''
    
    if earned > 0 and blessed != True:
        cursor.execute(edit, [(earned), (user_ping)])
        db.commit()
        await channel.send(crimes[randint(0, len(crimes) - 1)] + " and you earned $" + str(earned))
    elif earned < 0 and blessed != True:
        cursor.execute(edit, [(earned), (user_ping)])
        db.commit()
        await channel.send(failed_crimes[randint(0, len(failed_crimes) - 1)] + " and you lost $" + str(earned)[1:])
    elif blessed == True:
        earned = randint(1000, 50000)
        cursor.execute(edit, [(earned), (user_ping)])
        db.commit()
        await channel.send("You have been blessed by the artifact, and you earned $" + str(earned))