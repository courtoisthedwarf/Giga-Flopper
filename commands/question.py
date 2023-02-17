from random import randint

class info:
    name = "Questions"
    description = "Ask me a question"
    usage = "[Question Key Word]"

questions = [
    "is",
    "am",
    "does",
    "did",
    "are"
]

responses = [
    "Fuck off.", 
    "Yes.", 
    "Yes, and Rex is gay.", 
    "No.", 
    "Potentially.", 
    "I don't know.",
    "Shush."
]

def get_response():
    return responses[randint(0, len(responses))]
    