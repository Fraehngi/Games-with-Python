import time
from hangman.main import hangman_engine
from rock_paper_scissors.main import rps_runtime
from model.randomizer import Randomizer


def choose_game(number):
    """ This function gives the player the choice to pick a game from our
     game library. His choice starts the game then"""
    chosen_game = None
    if number == "0":
        games = ["1", "2"]
        random_number = Randomizer().generate_random(games)
        if random_number == "1":
            print("Great! Let's play a game of Hangman!")
            time.sleep(1)
            chosen_game = "hangman"
        elif random_number == "2":
            print("Great! Let's play a game of Rock, Paper, Scissors!")
            time.sleep(1)
            chosen_game = "rps"

    elif number == "1":
        print("Great! Let's play a game of Hangman!")
        time.sleep(1)
        chosen_game = "hangman"
    elif number == "2":
        print("Great! Let's play a game of Rock, Paper, Scissors!")
        time.sleep(1)
        chosen_game = "rps"

    # only use the actual game function once in this file, much easier to maintain!
    if chosen_game == "hangman":
        hangman_engine()
    else:
        rps_runtime()
