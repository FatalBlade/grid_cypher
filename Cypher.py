# Cypher.py
import settings
import string

def filter_word(word):
    """ This function filters given words for specified criteria """
    letters = {}
    
    for letter in word:
        if letter not in string.ascii_letters:
            print('A-z only, please try again.')
            return True
    if len(word) != 5:
        print('Word must be 5 characters long, please try again.')
        return True
    for letter in word:
        try:
            letters[letter] += 1
        except KeyError:
            letters[letter] = 1
    for number in letters.values():
        if number > 1:
            print('No repeating letters please try again.')
            return True
    return False

def get_word():
    """ This function prompts a user to input a word """
    flag_filter = True
    while flag_filter:
        word = input('Choose a 5 letter word with no ' +
                     'repeating letters or the letters j/k: ')
        flag_filter = filter_word(word) 
    return word


def create_cypher():
    """ This Function creates a one time Cypher from a given word """
    # This is the actual cypher itself at it's default a-z settings
    Cypher = { 11: 'a',  21: 'b',  31: 'c',  41: 'd',  51: 'e', 
               12: 'f',  22: 'g',  32: 'h',  42: 'i',  52: 'j/k',
               13: 'l',  23: 'm',  33: 'n',  43: 'o',  53: 'p',
               14: 'q',  24: 'r',  34: 's',  44: 't',  54: 'u',
               15: 'v',  25: 'w',  35: 'x',  45: 'y',  55: 'z' }
    # Default ordered list a-z
    Alpha = ['a', 'b', 'c', 'd', 'e',
            'f', 'g', 'h', 'i', 'j/k',
            'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']
    # Will eventually hold a string of the seperate letters of your word
    Key = []
    # DO NOT CHANGE // Controls the x/y axis' of the cypher
    Axis = [11, 21, 31, 41, 51,
            12, 22, 32, 42, 52,
            13, 23, 33, 43, 53,
            14, 24, 34, 44, 54,
            15, 25, 35, 45, 55]
    # Used to change which location on the cypher you're editing
    selector = 0
    if settings.debug:
        # This should say "A l e x" if Cypher is set up properly
        print(Cypher[11], Cypher[13], Cypher[51], Cypher[35])
        # This should result in the alphabet in order as a list
        print(Alpha)
    # Prompt user for word
    word = get_word()
    # Change to lowercase
    wordLower = word.lower()
    if settings.debug:
        # Verifies lowecase conversion
        print(wordLower)
    
    for letter in wordLower:
        # Removes the letters in word from alphabet
        Alpha.remove(letter)
            
    if settings.debug:
        # Verifies that all letters have been removed
        print(Alpha)
    
    for letter in wordLower:
        # Turns string into seperated list of letters
        Key.append(letter)
    
    if settings.debug:
        # Verifies that the word has been turned into a list properly
        print(Key)
    
    # adds the list of letters from word to the beginning of our alphabet
    Final = Key + Alpha
    
    if settings.debug:
        # Verifies proper letter order
        print(Final)
    
    for key in Cypher:
        # Changes a value in the default cypher to our new value
        Cypher[Axis[selector]] = Final[selector]
        # Increments which value we are editing
        selector = selector +1
    if settings.debug:
        # Verifies our dictionary cypher has been created properly
        print(Cypher)

