from settings import *


def initial_start():
    """This function welcomes the player printing a text from a
    .txt file"""

    first_words_location = RESOURCES_PATH / 'first_words.txt'
    with open(first_words_location, "r") as file:
        for i in file.readlines():
            print(i.strip())


def list_games():
    """This function lists all games from the library. It reads the
    players name and adds it to a string. Then it gives the player the
    library and some text from a .txt"""

    game_library_location = RESOURCES_PATH / 'game_library.txt'

    with open(game_library_location, "r") as file:
        for i in file.readlines():
            print(i.strip())


def picking_game():
    """This function let's the player choose a game to play and returns
    the input for later use"""

    pick_game = input("Type the number of the game you want to play: ").strip()
    if len(pick_game) == 1:
        if pick_game.isdigit():
            return True, pick_game

    return False, ""
