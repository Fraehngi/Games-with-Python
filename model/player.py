import json
from settings import *


class Player:
    """This class handles the creation of new players"""
    username = ""

    def __init__(self, username=""):
        self.username = username

    def check_player(self):
        """This function performs a check if the input already
        exists in the name_db or if it's a new player. A specific
        message is printed for either case"""

        if self.check_existing_player():
            print(f"Welcome back, {self.username}!"
                  f" You have been playing with us {self.get_times_played()} times!")
        else:
            self.save_new_player()
            print(f"Nice to meet you, {self.username}! "
                  f"This is your first time playing with us!")

    def check_existing_player(self):
        user_file = RESOURCES_PATH / "players" / f"{self.username}.json"
        if user_file.exists():
            self.handle_times_played()
            return True
        return False

    def save_new_player(self):
        gamer_db = {
            "username": self.username,
            "played": 1
        }

        with open(RESOURCES_PATH / "players" / f"{self.username}.json", "w") \
                as json_file:
            json.dump(gamer_db, json_file)

    def handle_times_played(self):
        user_file = RESOURCES_PATH / "players" / f"{self.username}.json"
        add_one = json.load(open(user_file))
        add_one["played"] = add_one["played"] + 1
        with open(user_file, "w") as added_game:
            json.dump(add_one, added_game)

    def get_times_played(self):
        get_times = json.load(open(RESOURCES_PATH / "players" / f"{self.username}.json"))
        times = get_times["played"]
        return times

    def prompt_name(self):
        """
        Prompt user for username
        """
        self.username = input("Please enter a name: ")
        return self.username
