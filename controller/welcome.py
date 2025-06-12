def welcome_handler():
    return 200, {"Content-Type": "application/json"}, b'{"message": "Welcome to the api in python !"}'
