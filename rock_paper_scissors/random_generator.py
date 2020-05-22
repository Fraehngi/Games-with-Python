from model.randomizer import Randomizer


def generate_weapon():
    """This function generates a random pick for the game to use"""

    weapons = ("Rock", "Paper", "Scissor")
    get_weapon = Randomizer().generate_random(weapons)
    return get_weapon


def get_player_weapon():
    """This function let's the player pick a weapon of choice. It also
     checks if it's a valid input and will force a new input if it's an
     invalid choice"""

    input_valid = True
    new_input = False
    while input_valid or new_input:
        player_weapon = input("Choose Rock, Paper or Scissor: ")
        if player_weapon == "Rock":
            return "Rock"
        elif player_weapon == "Paper":
            return "Paper"
        elif player_weapon == "Scissor":
            return "Scissor"
        else:
            print("That's not a valid choice. Please choose again!")
            input_valid = False
            new_input = True
