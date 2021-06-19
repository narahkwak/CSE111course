import random
# Create a list of strings and assign
# the list to a variable named words.
words = ["boy", "girl", "cat", "dog", "bird"]

# Call the random.choice function which will choose
# one string from the words list. Store the chosen
# string in a variable named word.
word = random.choice(words)

def main():
    print(f"a. {get_determiner(1)} {get_noun(1)} {get_verb(1 , 'past' )}")
    print(f"b. {get_determiner(2)} {get_noun(2)} {get_verb(2 , 'past' )}")
    print(f"c. {get_determiner(1)} {get_noun(1)} {get_verb(1 , 'present' )}")
    print(f"d. {get_determiner(2)} {get_noun(2)} {get_verb(2 , 'present' )}")
    print(f"e. {get_determiner(1)} {get_noun(1)} {get_verb(1 , 'future' )}")
    print(f"f. {get_determiner(2)} {get_noun(2)} {get_verb(2 , 'future' )}")
    print()
    print(f"a. {get_determiner(1)} {get_noun(1)} {get_verb(1 , 'past' )} {get_prepositional_phrase(1)}{get_punctuations()}")
    print(f"b. {get_determiner(2)} {get_noun(2)} {get_verb(2 , 'past' )} {get_prepositional_phrase(2)}{get_punctuations()}")
    print(f"c. {get_determiner(1)} {get_noun(1)} {get_verb(1 , 'present' )} {get_prepositional_phrase(1)}{get_punctuations()}")
    print(f"d. {get_determiner(2)} {get_noun(2)} {get_verb(2 , 'present' )} {get_prepositional_phrase(2)}{get_punctuations()}")
    print(f"e. {get_determiner(1)} {get_noun(1)} {get_verb(1 , 'future' )} {get_prepositional_phrase(1)}{get_punctuations()}")
    print(f"f. {get_determiner(2)} {get_noun(2)} {get_verb(2 , 'future' )} {get_prepositional_phrase(2)}{get_punctuations()}")

def get_determiner(quantity):
    """Return a randomly chosen determiner. A determiner is a word
    like "the", "a", "one", "two", "some", "many". If quantity == 1,
    this function will return either "the" or "one". Otherwise
    this function will return either "some" or "many".

    Parameter
        quantity: an integer. If quantity == 1, this function will
            return a determiner for a singular noun. Otherwise this
            function will return a determiner for a plural noun.
    Return: a randomly chosen determiner.
    """
    if quantity == 1:
        words = ["the", "one"]
    else:
        words = ["some", "many"]

    # Randomly choose and return a determiner.
    word = random.choice(words)
    return word

def get_noun(quantity):
    if quantity == 1:
        nouns = ["adult", "bird", "boy", "car", "cat", "child", "dog", "girl", "man", "woman"]
    else:
        nouns = ["adults", "birds", "boys", "cars", "cats", "children", "dogs", "girls", "men", "women"]
    
    noun = random.choice(nouns)
    return noun

def get_verb(quantity, tense):
    if tense == "past":
        verbs = ["drank", "ate", "grew", "laughed", "thought", "ran", "slept", "talked", "walked", "wrote"]
    if tense == "present" and quantity == 1:
        verbs = ["drinks", "eats", "grows", "laughs", "thinks","runs", "sleeps", "talks", "walks", "writes"]
    if tense == "present" and quantity != 1:
        verbs = ["drink", "eat", "grow", "laugh", "think", "run", "sleep", "talk", "walk", "write"]
    if tense == "future":
        verbs = ["will drink", "will eat", "will grow", "will laugh","will think", "will run", "will sleep", "will talk", "will walk", "will write"]

    verb = random.choice(verbs)
    return verb

def get_preposition():
    preposition_list = ["about", "above", "across", "after", "along","around", "at", "before", "behind", "below","beyond", "by", "despite", "except", "for","from", "in", "into", "near", "of","off", "on", "onto", "out", "over","past", "to", "under", "with", "without"]
    preposition = random.choice(preposition_list)
    return preposition

def get_punctuations():
    punctuation_list = [".", "?", "!", ",", ";"]
    punctuation = random.choice(punctuation_list)
    return punctuation

"""Build and return a prepositional phrase composed of three
    words: a preposition, a determiner, and a noun by calling the
    get_preposition, get_determiner, and get_noun functions.

    Parameter
        quantity: an integer that determines if the
            determiner and nouns are singular or plural.
    Return: a prepositional phrase.
    """
def get_prepositional_phrase(quantity):
    if quantity == 1:
        preposition = get_preposition()
        determiner = get_determiner(1)
        noun = get_noun(1)
    elif quantity == 2:
        preposition = get_preposition()
        determiner = get_determiner(2)
        noun = get_noun(2)  

    prepositional_phrase = preposition + " " + determiner + " " + noun
    return prepositional_phrase

    



main()