import sys
try:
    resetoken = sys.argv[1]
    if resetoken == "reset":
        with open(".env","w") as tokenreseter:
            tokenreseter.write("TOKEN = ")
            tokenreseter.close()
        print("Token reset done")


except IndexError:
    try:
        import requests
        import discord
        import dotenv
    except ModuleNotFoundError:
        os.system("pip3 install -r requrirements.txt")
        os.system("pip install -r requirements.txt")     
    import bot
    import func as f
    import os
    import sys
    if __name__ == "__main__":
        f.sitechecker()
        #run the bot
        f.firsttimetokenchecker()


        
        # sys.exit("Testing")
        bot.run_discord_bot()