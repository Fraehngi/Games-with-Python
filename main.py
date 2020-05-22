# This is a collection of some games I've made
# for the purpose of learning to code with Python3

# You can pick one of three games in total. Let's go!

# To begin, just start this .py file


import time
from general.welcome_player import initial_start, list_games, picking_game
from general.game_decison import choose_game
from general.shut_down import end_program
from model.player import Player

initial_start()  # print a hearty welcome
time.sleep(1)

# get player
player = Player()
# get the players name, by prompting
gamer_name = player.prompt_name()
player.check_player()

time.sleep(1)

gaming_active = True
while gaming_active:
    list_games()  # talk to the player by name, list games
    game_pick_result, make_decision = picking_game()  # pick a game to play
    # check if the input was valid, before starting that game
    if game_pick_result:
        choose_game(make_decision)  # start picked game
        keep_gaming = input("Continue the fun and pick another game? y / n > ")
        if keep_gaming.lower() == "y":
            print("Great! You know the drill!")
        else:
            gaming_active = False
    else:
        print("Only type a number")

end_program()
time.sleep(10)
