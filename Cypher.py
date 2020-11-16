# cypher.py
import settings as config
import string
import sys
from time import sleep


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

def filter_message(message, index):
    """ This function filters given words for specified criteria """
    # letters = {}
    
    for letter in message:
        if letter not in string.ascii_letters:
            print('A-z only, please try again.')
            return True
    if len(message) > (len(index)/2):
        print('Your message is too long you need more bytes, please restart program')
        sleep(10)
        sys.exit()
    """"
    for letter in message:
        try:
            letters[letter] += 1
        except KeyError:
            letters[letter] = 1
    for number in letters.values():
        if number > 1:
            print('No repeating letters please try again.')
            return True
            """
    return False

def get_message(index):
    """ This function prompts a user to input a word """
    flag_filter = True
    while flag_filter:
        message_input = input('Please type out your message here: ')
        message_lower = message_input.lower()
        message = message_lower.replace(" ", "")
        flag_filter = filter_message(message, index)
    return (message, index)

def create_cypher():
    """ This Function creates a one time cypher from a given word """
    settings = config.settings()
    # This is the actual cypher itself at it's default a-z settings
    cypher = settings.cypher
    # Default ordered list a-z
    alpha = settings.alpha
    # Will eventually hold a string of the seperate letters of your word
    key = []
    # Used to change which location on the cypher you're editing
    selector = 0
    if settings.debug:
        # This should say "A l e x" if cypher is set up properly
        print(cypher[11], cypher[13], cypher[51], cypher[35])
        # This should result in the alphabet in order as a list
        print(alpha)
    # Prompt user for word
    word = get_word()
    # Change to lowercase
    wordLower = word.lower()
    if settings.debug:
        # Verifies lowecase conversion
        print(wordLower)
    
    for letter in wordLower:
        # Removes the letters in word from alphabet
        alpha.remove(letter)
            
    if settings.debug:
        # Verifies that all letters have been removed
        print(alpha)
    
    for letter in wordLower:
        # Turns string into seperated list of letters
        key.append(letter)
    
    if settings.debug:
        # Verifies that the word has been turned into a list properly
        print(key)
    
    # adds the list of letters from word to the beginning of our alphabet
    Final = key + alpha
    
    if settings.debug:
        # Verifies proper letter order
        print(Final)
    
    for key in cypher:
        # Changes a value in the default cypher to our new value
        cypher[settings.AXIS[selector]] = Final[selector]
        # Increments which value we are editing
        selector = selector +1
    if settings.debug:
        # Verifies our dictionary cypher has been created properly
        print(cypher)
    return cypher

def encrypt(cypher, index):
    """ This function will encrypt a given message using the generated cypher """
    message = get_message(index)

    return message
