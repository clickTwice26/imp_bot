import func
def handle_response(message):
    p_message = message.lower()

    if p_message == "-players":
        return func.playerOnline()
    
# def handle_response(message):
#     p_message = message.lower()

#     if p_message == "-players":
#         return "hellor"