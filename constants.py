
from dotenv import dotenv_values
token = dotenv_values(".env")["TOKEN"]


api_prefix = "https://api.mcstatus.io/v2/status/java/"
try:
    site = open("site.txt", "r").read()
except FileNotFoundError:
    pass

command_prefix = "-"
debug = False
debug_global = True
log_filename = "log.txt"