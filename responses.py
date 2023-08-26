import func
def handle_response(message):
    p_message = message.lower()

    if p_message == "players":
        return func.playerOnline()
    if p_message.startswith("changeip"):

        ip = p_message.split(" ")[1]
        try:
            with open("site.txt", "w") as siter:
                siter.write(ip)
                siter.close()
            return "```Your ip has been changed```"
        except:
            return "```Facing Error```"
    else:
        pass
# def handle_response(message):
#     p_message = message.lower()

#     if p_message == "-players":
#         return "hellor"