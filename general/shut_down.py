from settings import *


def end_program():
    """This functions ends the program and prints a nice text."""

    last_words_location = RESOURCES_PATH / "last_words.txt"
    with open(last_words_location, "r") as file:
        for i in file.readlines():
            print(i.strip())
