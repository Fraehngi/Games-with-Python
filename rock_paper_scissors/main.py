from rock_paper_scissors.random_generator import generate_weapon, get_player_weapon
from rock_paper_scissors.engine import rps_engine, shout

def rps_runtime():
    """This functions runs the rock paper scissors game. It combines our
    other functions into the working game all together. It reads the random
    generated pick of the game and the input from the player and compares
    them against each other. After the game it asks the user if he wants
    to play again or ends the rock paper scissors game"""

    play_rps = True
    while play_rps:
        bot = generate_weapon()
        player = get_player_weapon()
        shout()
        rps_engine(bot, player)
        more_rps = input("Another round? y / n > ")
        if more_rps == "y":
            print("Let's play another round!")
        else:
            play_rps = False