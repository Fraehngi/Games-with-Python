import time


def rps_engine(bot, player):
    """This function checks if the program or the player
    won based on their picks and prints the result of the game"""

    if bot == player:
        print("Draw! You both picked %s" % bot)
    elif bot != player:
        if bot == "Rock" and player == "Scissor":
            print("You've lost. Rock beats Scissor!")
        elif bot == "Paper" and player == "Rock":
            print("You've lost. Paper beats Rock!")
        elif bot == "Scissor" and player == "Paper":
            print("You've lost. Scissor beats Paper!")
        elif player == "Rock" and bot == "Scissor":
            print("You've won! Rock beats Scissor!")
        elif player == "Paper" and bot == "Rock":
            print("You've won! Paper beats Rock!")
        elif player == "Scissor" and bot == "Paper":
            print("You've won! Scissor beats Paper!")


def shout():
    """This function shouts ROCK! PAPER! SCISSOR! With a
    delay of .5 seconds"""

    time.sleep(0.5)
    print("ROCK!")
    time.sleep(0.5)
    print("PAPER!")
    time.sleep(0.5)
    print("SCISSORS!")
    time.sleep(0.5)