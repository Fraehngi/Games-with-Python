import random


class Randomizer:
    """This class is a simple random choice generator for
    repeated usage"""

    def generate_random(self, choices=list()):
        return random.choice(choices)

    def get_random_word(self, from_file=None):
        """This function will pick a random word from within our
        pre defined list of words and returns it for further use"""

        if from_file is None or from_file == "":
            word_list = ["Car", "Bicycle", "Train",
                         "Scooter", "Ship", "Skateboard"]
        else:
            word_list = list()
            with open(from_file, "r") as words:
                for word in words.readlines():
                    word_list.append(word.strip())

        randomize = self.generate_random(word_list).lower()
        return randomize
