from settings import *

# defined location of player database for later usage
names_location = RESOURCES_PATH / "name_db.txt"


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
            print(f"Welcome back, {self.username}!")
        else:
            self.save_new_player()
            print(f"Nice to meet you, {self.username}! "
                  f"It's your first time playing with us!")

    def check_existing_player(self):
        with open(names_location, "r") as saved_players:
            if self.username in saved_players.read():
                return True
            return False

    def save_new_player(self):
        with open(names_location, "a+") as saved_players:
            saved_players.write(self.username + "\n")

    def prompt_name(self):
        """
        Prompt user for username
        """
        self.username = input("Please enter a name: ")
        return self.username
