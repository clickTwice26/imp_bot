
from dotenv import dotenv_values
token = dotenv_values(".env")["TOKEN"]

url = "https://discord.com/api/oauth2/authorize?client_id=1144865343567822889&permissions=2183991392320&scope=bot"

api_prefix = "https://api.mcstatus.io/v2/status/java/"
site = open("site.txt", "r").read()
with open("log.txt", "w") as logger:
    logger.write(api_prefix+site)
    logger.close()