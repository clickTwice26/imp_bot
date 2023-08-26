url = "https://discord.com/api/oauth2/authorize?client_id=1144865343567822889&permissions=2183991392320&scope=bot"
token = "MTE0NDg2NTM0MzU2NzgyMjg4OQ.GIEGIK.yOEvjuZqlgnqk4oP73REmjhJarWyfnRZEr3DGI"
api_prefix = "https://api.mcstatus.io/v2/status/java/"
site = open("site.txt", "r").read()
with open("log.txt", "w") as logger:
    logger.write(api_prefix+site)
    logger.close()