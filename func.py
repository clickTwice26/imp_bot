import requests as req
import constants as C
import json
def playerOnline():
    data = req.get(C.api_prefix+C.site)
    # with open("data.txt", "w") as writer:
    #     writer.write(data.text)
    #     writer.close()

    test_data = json.loads(data.text)
    # print(type(test_data))

    total_online_players = test_data["players"]["online"]
    total_number = total_online_players
    
    if total_online_players > 0:

        total_online_players = test_data["players"]["list"]
        print(total_online_players)
        print(len(total_online_players))
        counter = 0
        player_list = []
        for i in total_online_players:
            print(i["name_raw"])
            player_list.append(i["name_raw"])
        players_data = ",".join(player_list)
        total_number = len(player_list)
        
    else:
        total_number = 0
        players_data = "No Online Players"
    print("Total Online Players:", total_number)
    print("Online Players:", players_data)
    output = f"""
    ```
    Total Online PLayers: {total_number}
    Players: {players_data}
    ```
    """
    return output