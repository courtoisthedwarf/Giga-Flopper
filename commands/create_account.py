import sqlite3

with sqlite3.connect("economy.db") as db:
    cursor = db.cursor()


class info:
    name = "Create Account"
    description = "Creates user if you don't already have one"
    usage = "create account"


async def run(user_ping, channel, args):
    cursor.execute('''SELECT * FROM users''')
    users = cursor.fetchall()

    for user in users:
        if user[1] == user_ping:
            return "You already have an account bozo."
            
            
    add = '''
INSERT INTO users(discordID, money, items, last_robbed)
VALUES(?,0,"credit card", 0)
'''
    cursor.execute(add, [user_ping])
    db.commit()

    channel.send("Welcome " + user_ping)