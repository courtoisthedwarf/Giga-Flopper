from random import randint

class info:
    name = "Gay test"
    description = "Tests someone for how gay they are"
    usage = "gay test [@user]"

def get_gayness(user):
    if user == "<@796834786580103179>":
        return "100%"
    elif user == "<@1070730197302771792>":
        return "1000%"
    else:
        number = str(randint(0, 100))
        return number + "% gay"