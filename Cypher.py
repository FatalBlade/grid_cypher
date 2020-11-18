# cypher.py
import settings as config
import string
import sys
from time import sleep


def filter_word(word):
    """ This function filters given words for specified criteria """
    letters = {}
    # Filters for any characters not A-Z, a-z
    for letter in word:
        if letter not in string.ascii_letters:
            print('A-z only, please try again.')
            return True
    # Filters for words not exactly 5 characters long
    if len(word) != 5:
        print('Word must be 5 characters long, please try again.')
        return True
    # Filers for repeating letters
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
        # Prompts user for the cypher key
        word = input('Choose a 5 letter word with no ' +
                     'repeating letters or the letters j/k: ')
        # Runs the word through various criteria filters
        flag_filter = filter_word(word) 
    return word

def filter_message(message, index):
    """ This function filters given words for specified criteria """
    # Filters for any characters not A-Z, a-z
    for letter in message:
        if letter not in string.ascii_letters:
            print('A-z only, please try again.')
            return True
    # Filters messages for lengths longer than available characters in page
    if len(message) > (len(index)/2):
        print('Your message is too long you need more bytes, please restart program')
        # Waits 10 seconds to allow user to read above
        sleep(10)
        # Force ends program
        sys.exit()
    return False

def get_message(index):
    """ This function prompts a user to input a word """
    settings = config.settings()
    flag_filter = True
    while flag_filter:
        # Prompts user for a message to encrypt
        message_input = input('Please type out your message here: ')
        # Sets message to all lowercase
        message_lower = message_input.lower()
        # Strips all whitespace from message
        message = message_lower.replace(" ", "")
        # Runs message through various criteria filters
        flag_filter = filter_message(message, index)
    if settings.debug:
        print('\n')
        print('Direct output: ' + message_input) # Direct output
        print('Lowercase output: ' + message_lower) # Lowercase output
        print('Stripped output: ' + message) # Stripped whitespace output
    return (message, index)

# function to return key for any value
def get_key(cypher, val):
    for key, value in cypher.items():
         if val == value:
             return key
    return "key doesn't exist"

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
        # This should say "f a t a l b l a d e" if cypher is set up properly
        print('This should say fatalblade: ', end='')
        print(cypher[12], cypher[11], cypher[44], cypher[11], cypher[13],
              cypher[21], cypher[13], cypher[11], cypher[41], cypher[51])
        # This should result in the alphabet in order as a list
        print('\n')
        print('Alphabet as list: ', end='')
        print(alpha)
        print('\n')
    # Prompt user for word
    word = get_word()
    # Change to lowercase
    wordLower = word.lower()
    if settings.debug:
        # Verifies lowecase conversion
        print('\n')
        print('Lowercase word: ' + wordLower)
    
    for letter in wordLower:
        # Removes the letters in word from alphabet
        alpha.remove(letter)
            
    if settings.debug:
        # Verifies that all letters have been removed
        print('\n')
        print('Striped alphabet: ', end='')
        print(alpha)
    for letter in wordLower:
        # Turns string into seperated list of letters
        key.append(letter)
    
    if settings.debug:
        # Verifies that the word has been turned into a list properly
        print('\n')
        print('Keyword: ', end='')
        print(key)

    # adds the list of letters from word to the beginning of our alphabet
    Final = key + alpha
    
    if settings.debug:
        # Verifies proper letter order
        print('\n')
        print('Final alphabet: ', end='')
        print(Final)
    
    for key in cypher:
        # Changes a value in the default cypher to our new value
        cypher[settings.AXIS[selector]] = Final[selector]
        # Increments which value we are editing
        selector = selector +1
    if settings.debug:
        # Verifies our dictionary cypher has been created properly
        print('\n')
        print('Edited cypher: ', end='')
        print(cypher)
    return cypher

def encrypt(cypher, index):
    """ This function will encrypt a message using the generated cypher """
    message = get_message(index)
    encrypted = ''
    for letter in message[0]:
        encrypted = encrypted + str(get_key(cypher, letter))
    return encrypted
