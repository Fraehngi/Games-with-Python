# import json
# from settings import *
#
#
# def manage_player(gamer_name):
#     gamer_db = {
#         "username": gamer_name,
#         "played": 0
#     }
#     with open(RESOURCES_PATH / "players" / f"{gamer_name}.json", "w") as json_file:
#         json.dump(gamer_db, json_file)
#
#     loaded_gamer_db = {}
#
#     with open(RESOURCES_PATH / "players" / f"{gamer_name}.json", "r") as json_file:
#         loaded_gamer_db = json.load(json_file)
#     print(loaded_gamer_db["played"])
