import requests as req
import constants as C
import json
import sys
from datetime import datetime

def line_prepender(filename, string):
    with open(filename, 'r+') as f:
        content = f.read()
        f.seek(0, 0)
        f.write(string.rstrip('\r\n') + '\n' + content)
def debug(comment, active="false"):
    if active not in ["true","false"]:
        print("[+] Debug prompt not successful")
    elif active == "false":
        # print("")
        pass
    elif active == "true":
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        dt_string = str(dt_string)
        string = f"[+] Time: {dt_string} | {comment}\n"
        filename = C.log_filename
        line_prepender(filename, string)




    else:
        print("[+] Attempting Debug Prompt from CONSTANT")
        if C.debug_global is True:
            if C.debug is True:
                print("Globally debugging on")
                now = datetime.now()
                dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
                dt_string = str(dt_string)
                string = f"[+] Time: {dt_string} | {comment}\n"
                filename = C.log_filename
                line_prepender(filename, string)
            else:
                print("Globally debugging off")
        else:
            print("[+] Debug prompt not successful[x2]")
    


def playerOnline():
    data = req.get(C.api_prefix+C.site)
    # with open("data.txt", "w") as writer:
    #     writer.write(data.text)
    #     writer.close()
    debug(data.text, "false")
    test_data = json.loads(data.text)
    debug(test_data, "false")
    # print(type(test_data))

    total_online_players = test_data["players"]["online"]
    total_number = total_online_players
    
    if total_online_players > 0:

        total_online_players = test_data["players"]["list"]
        # print(total_online_players)
        # print(len(total_online_players))
        counter = 0
        player_list = []
        for i in total_online_players:
            # print(i["name_raw"])
            player_list.append(i["name_raw"])
        players_data = ",".join(player_list)
        total_number = len(player_list)
        
    else:
        total_number = 0
        players_data = "No Online Players"
    # print("Total Online Players:", total_number)
    # print("Online Players:", players_data)
    output = f"""
    ```
    Total Online PLayers: {total_number}
    Players: {players_data}
    ```
    """
    return output
def playerOnlineCounter():
    data = req.get(C.api_prefix+C.site)
    # with open("data.txt", "w") as writer:
    #     writer.write(data.text)
    #     writer.close()

    test_data = json.loads(data.text)
    # print(type(test_data))

    total_online_players = test_data["players"]["online"]
    max_player = test_data["players"]["max"]
    total_number = str(total_online_players)+"/"+str(max_player)
 
    return total_number
