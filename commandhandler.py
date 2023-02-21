import os

commands = os.listdir(os.getcwd() + "/commands")

for command in commands:
    if command.endswith(".py"):
        execute = ("import commands." + command.split(".")[0])
        exec(execute)
        print(f'Loading {command.split(".")[0].replace("_", " ")}...')

    elif command != "__pycache__": # Also known as an organisation im not allowed to name
        for child_command in os.listdir(f'{os.getcwd()}/commands/{command}'):
            if child_command.endswith(".py"):
                exec(f'import commands.{command}.{child_command.split(".")[0]}')
                print(f'Loading {command.split(".")[0].replace("_", " ")}...')

async def handle(message: str, userID, channel) -> str:
    user_ping = f'<@{userID}>'
    
    commands_list = os.listdir(os.getcwd() + "/commands")

    p_message = message.lower()

    for command in commands_list:
        if command.endswith(".py"):    
            command = command.split(".py")[0]
            formatted_message = p_message.replace(" ", "_")
            if command in formatted_message:
                issued_command = command
                args = formatted_message.split(issued_command)[1].replace("_", " ")[1:].split(" ")

                execute = f'commands.{command}.run("{user_ping}", channel, {args})'
                await eval(execute)