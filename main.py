import bot
import func as f
import os
if __name__ == "__main__":
    #run the bot
    f.firsttimetokenchecker()
    try:
        import requests
        import discord
        import dotenv
    except ModuleNotFoundError:
        os.system("pip3 install -r requrirements.txt")
        os.system("pip install -r requirements.txt")        

    bot.run_discord_bot()