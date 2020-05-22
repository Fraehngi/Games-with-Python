def word_underscore(fill):
    """This function will print our initial pattern of underscores
    to give the player an idea of the word length"""

    word_length = len(fill)
    print(f"I'm thinking of an vehicle with {word_length} characters!")
    random_word_underscore = ""
    for i in fill:
        random_word_underscore += "_ "
    print(random_word_underscore)
