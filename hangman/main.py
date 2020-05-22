from hangman.random_generator import word_underscore
from hangman.guess_mechanic import user_guess, game_end

from model.randomizer import Randomizer
from settings import *


def hangman_engine():
    """This functions runs the hangman game. It combines our other
    functions into the working game all together. It places the random
    picked word into our guess mechanic. After a game it asks the user
    if he wants to play again or ends the hangman game"""

    play_hangman = True
    while play_hangman:
        # get a random word from a file, for hangman i use dictionary.txt
        picked_word = Randomizer().get_random_word(
            from_file=RESOURCES_PATH / "dictionary.txt")

        word_underscore(picked_word)
        did_win = user_guess(picked_word)
        game_end(did_win)
        more_hangman = input("Another round? y / n > ")
        if more_hangman == "y":
            print("Let's play another round!")
        else:
            play_hangman = False
