
from dotenv import dotenv_values
token = dotenv_values(".env")["TOKEN"]


api_prefix = "https://api.mcstatus.io/v2/status/java/"
site = open("site.txt", "r").read()

command_prefix = "-"
debug = False
debug_global = True
log_filename = "log.txt"