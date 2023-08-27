
from dotenv import dotenv_values
token = dotenv_values(".env")["TOKEN"]


api_prefix = "https://api.mcstatus.io/v2/status/java/"
site = open("site.txt", "r").read()
with open("log.txt", "w") as logger:
    logger.write(api_prefix+site)
    logger.close()
command_prefix = "-"