import os

commands = os.listdir(os.getcwd() + "/Giga-Flopper/commands")

for file in commands:
    if file.endswith(".py"):
        execute = ("import commands." + file.split(".")[0])
        exec(execute)
        print(f'Loading {file.split(".")[0].replace("_", " ")}...')

    elif file != "__pycache__": # Also known as an organisation im not allowed to name
        for file2 in os.listdir(f'{os.getcwd()}/Giga-Flopper/commands/{file}'):
            if file2.endswith(".py"):
                exec(f'import commands.{file}.{file2.split(".")[0]}')
                print(f'Loading {file.split(".")[0].replace("_", " ")}...')

async def handle(message: str, userID, channel) -> str:
    user_ping = f'<@{userID}>'
    
    commands_list = os.listdir(os.getcwd() + "/Giga-Flopper/commands")

    p_message = message.lower()

    for file in commands_list:
        if file.endswith(".py"):    
            command = file.split(".py")[0]
            formatted_message = p_message.replace(" ", "_")
            if command in formatted_message:
                issued_command = command
                args = formatted_message.split(issued_command)[1].replace("_", " ")[1:].split(" ")

                execute = f'commands.{command}.run("{user_ping}", channel, {args})'
                await eval(execute)