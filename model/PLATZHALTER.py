# gamer_db = {
#     "username": player.username,
#     "played": 0
# }
# with open(os.path.join(RESOURCES_PATH, f"{gamer_name}.json"), "w") as json_file:
#     json.dump(gamer_db, json_file)
#
# loaded_gamer_db = {}
#
# with open(os.path.join(RESOURCES_PATH, f"{gamer_name}.json"), "r") as json_file:
#     loaded_gamer_db = json.load(json_file)
# print(loaded_gamer_db["played"])