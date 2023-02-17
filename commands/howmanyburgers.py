from random import randint

class info:
    name = "How many burgers"
    description = "Returns their burger count"
    usage = "how many burgers [@user]"

def get_burgers(user):
    if user == "<@799198085632753674>":
        return "ALL OF EM"
    else:
        return randint(0, 20)