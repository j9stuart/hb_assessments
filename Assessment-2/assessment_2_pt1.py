"""Dictionaries Assessment

**IMPORTANT:** these problems are meant to be solved using
dictionaries and sets.
"""

def count_words(phrase):
    """Count unique words in a string.

    This function should take a single string and return a dictionary
    that has all of the distinct words as keys, and the number of
    times that word appears in the string as values.

    For example::

        >>> print_dict(count_words("each word appears once"))
        {'appears': 1, 'each': 1, 'once': 1, 'word': 1}

    Words that appear more than once should be counted each time::

        >>> print_dict(count_words("rose is a rose is a rose"))
        {'a': 2, 'is': 2, 'rose': 3}

    It's fine to consider punctuation part of a word (e.g., a comma
    at the end of a word can be counted as part of that word) and
    to consider differently-capitalized words as different::

        >>> print_dict(count_words("Porcupine see, porcupine do."))
        {'Porcupine': 1, 'do.': 1, 'porcupine': 1, 'see,': 1}
    """
    #change string to list of words"
    phrase = phrase.split()

    word_dictionary = {}

    #iterate through the list of words and adds words to dictionary if not there
    # and sets the value to zero, if word is in dictionary, add 1 to value. 
    for word in phrase:
        if word in word_dictionary:
            word_dictionary[word] += 1
        else:
            word_dictionary[word] = 1

    return word_dictionary



def get_melon_price(melon_name):
    """Given a melon name, return the price of the melon

    Here are a list of melon names and prices:
    Watermelon 2.95
    Cantaloupe 2.50
    Musk 3.25
    Christmas 14.25
    (it was a bad year for Christmas melons -- supply is low!)

        >>> get_melon_price('Watermelon')
        2.95

        >>> get_melon_price('Musk')
        3.25

        >>> get_melon_price('Tomato')
        'No price found'
    """
    #creates dictionary of melon names and prices
    melon_inventory = {"Watermelon": 2.95, "Cantaloupe": 2.50, "Musk": 3.25, "Christimas": 14.25}

    #if melong_name is in dictionary, returns melon price; if not, prints No price found
    if melon_name in melon_inventory:
        return melon_inventory[melon_name]
    else:
        print "'No price found'"


def word_length_sorted(words):
    """Return list of word-lengths and words.

    Given a list of words, return a list of tuples, ordered by
    word-length. Each tuple should have two items --- a number that
    is a word-length, and the list of words of that word length.

    In addition to ordering the list by word length, order each
    sub-list of words alphabetically.

    For example::

        >>> word_length_sorted(["ok", "an", "apple", "a", "day"])
        [(1, ['a']), (2, ['an', 'ok']), (3, ['day']), (5, ['apple'])]
    """
    #Create empty word dictionary
    word_dict = {}

    #Create empty list of word tuples
    word_tuples = []

    #iterates through list of words and adds length of word to dictionary if not present, 
    #if length of word is in dictionary adds word to list of words that length
    for word in words:
        if len(word) not in word_dict:
            word_dict[len(word)] = [word]
        else:
            word_dict[len(word)] += [word]


    #iterates through dictionary keys to create a list of tuples; sorts list of words in values
    for key in word_dict:
        word_tuples.append((key, sorted(word_dict[key])))

    #sorts word tuples by length
    sorted_word_tuples = sorted(word_tuples)

    return sorted_word_tuples
   

word_length_sorted(["love", "life", "liberty", "happiness", "laugh", "like"])


def translate_to_pirate_talk(phrase):
    """Translate phrase to pirate talk.

    Given a phrase, translate each word to the Pirate-speak
    equivalent. Words that cannot be translated into Pirate-speak
    should pass through unchanged. Return the resulting sentence.

    Here's a table of English to Pirate translations:

    ----------  ----------------
    English     Pirate
    ----------  ----------------
    sir         matey
    hotel       fleabag inn
    student     swabbie
    man         matey
    professor   foul blaggart
    restaurant  galley
    your        yer
    excuse      arr
    students    swabbies
    are         be
    restroom    head
    my          me
    is          be
    ----------  ----------------

    For example::

        >>> translate_to_pirate_talk("my student is not a man")
        'me swabbie be not a matey'

    You should treat words with punctuation as if they were different
    words::

        >>> translate_to_pirate_talk("my student is not a man!")
        'me swabbie be not a man!'
    """

    #Create a dictionary for translations
    english_pirate_dict = { "sir": "matey", 
                            "hotel": "fleabag inn", 
                            "student": "swabbie", 
                            "man": "matey", 
                            "professor": "foul blaggart", 
                            "restaurant": "galley", 
                            "your": "yer",
                            "excuse": "arr",
                            "students": "swabbies",
                            "are": "be",
                            "restroom": "head",
                            "my": "me",
                            "is": "be",
                            }

    #Make phrase a list
    phrase = phrase.split()

    #Create empty list
    first_draft = []

    #Iterate through words and append values to list for translation
    for word in phrase:
        if word in english_pirate_dict:
            first_draft.append(english_pirate_dict[word])
        else:
            first_draft.append(word)

    #joins list with space
    translation = " ".join(first_draft)

    return translation


translate_to_pirate_talk("my student is not a man!")


def kids_game(names):
    """Play a kids' word chain game.

    Given a list of names, like::

      bagon baltoy yamask starly nosepass kalob nicky

    Do the following:

    1. Always start with the first word ("bagon", in this example).

    2. Add it to the results.

    3. Use the last letter of that word to look for the next word.
       Since "bagon" ends with n, find the *first* word starting
       with "n" in our list --- in this case, "nosepass".

    4. Add "nosepass" to the results, and continue. Once a word has
       been used, it can't be used again --- so we'll never get to
       use "bagon" or "nosepass" a second time.

    5. When you can't find an unused word to use, you're done!
       Return the list of output words.

    For example::

        >>> kids_game(["bagon", "baltoy", "yamask", "starly",
        ...            "nosepass", "kalob", "nicky", "booger"])
        ['bagon', 'nosepass', 'starly', 'yamask', 'kalob', 'baltoy']

    (After "baltoy", there are no more y-words, so we end, even
    though "nicky" and "booger" weren't used.)

    Another example:

        >>> kids_game(["apple", "berry", "cherry"])
        ['apple']

    This is a tricky problem. In particular, think about how using
    a dictionary (with the super-fast lookup they provide) can help;
    good solutions here will definitely require a dictionary.
    """
    index = 0
    results = [names[0]]
    dict_of_names = {}
    new_name = names[0]
    old_name = ""
    
    #iterates through name list adds name and first letter to dictionary if first
    #letter not present. Removes word from list if the first letter is already there.
    for name in names[1:]:
        if name[0] not in dict_of_names:
            dict_of_names[name[0]] = name
        else:
            names.remove(name)


    #While the last letter of the current word is in the dictionary, appends word match(value)
    #of last letter(key) and then deletes the key from the dictionary. 
    while new_name[-1] in dict_of_names:
        old_name = new_name[-1]
        results.append(dict_of_names[new_name[-1]])
        new_name = dict_of_names[new_name[-1]]
        del dict_of_names[old_name[-1]]

    return results
            



kids_game(['bagon', 'baltoy', 'yamask', 'starly', 'nosepass', 'kalob', 'nicky'])

#####################################################################
# You can ignore everything below this.

def print_dict(d):
    # This method is used to print dictionaries in key-alphabetical
    # order, and is only for our doctests. You can ignore it.
    if isinstance(d, dict):
        print "{" + ", ".join(
            "%r: %r" % (k, d[k]) for k in sorted(d)) + "}"
    else:
        print d


def sort_pairs(l):
    # Print sorted list of pairs where the pairs are sorted. This is
    # used only for documentation tests. You can ignore it.
    return sorted(sorted(pair) for pair in l)


if __name__ == "__main__":
    print
    import doctest
    if doctest.testmod().failed == 0:
        print "*** ALL TESTS PASSED ***"
    print
