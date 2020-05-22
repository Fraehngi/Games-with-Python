from model.attempts import Attempts


def user_guess(random_word):
    """This function is running the guess mechanic for our game.
    It let's the player pick a character to look for. It checks if the
    input is in the alphabet and will ask for a new input, if it's not
    a character from A to Z. Further it will check if the player does
    look for a single character or maybe fills in the final word we're
    looking for. Also we have a counter for the remaining attempts"""

    finished = False
    right_guess = False
    user_guesses = list()
    tries = Attempts(random_word).remaining_attempts() + 1

    while not finished:
        final_word = ""
        tries += - 1
        print(f"You have {tries} attempts remaining!")
        new_guess = input("Guess a character: ").lower()

        if new_guess.isalpha():
            if len(new_guess) > 1:
                user_guesses.append("1")

                if new_guess == random_word:
                    right_guess = True
                    finished = True
                    break

            else:
                user_guesses.append(new_guess)
                for char in random_word:
                    if new_guess == char or char in user_guesses:
                        final_word += char
                    else:
                        final_word += "_ "

                    if len(user_guesses) >= len(random_word) \
                            or final_word == random_word:
                        finished = True

                    if final_word == random_word:
                        right_guess = True

        else:
            user_guesses.append("1")
            print("Oops. Guess must be A - Z!")

            if len(user_guesses) >= len(random_word) \
                    or final_word == random_word:
                finished = True

        print(final_word.capitalize())

    return right_guess


def game_end(right_guess):
    """This function checks if the player has lost or won"""

    if right_guess:
        print(f"Good job! You've guessed the right word!")
    else:
        print(f"Better luck next time!")
