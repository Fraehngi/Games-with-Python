
class Attempts:
    """This class counts and returns the length of the input
    for later usage in multiple scripts"""

    def __init__(self, number):
        self.number = len(number)

    def remaining_attempts(self):
        max_attempts = self.number
        return max_attempts
