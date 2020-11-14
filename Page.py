# Page.py

import random
import string
import settings as config



def create_page(bytes):
    """ This function creates the one time page  """
    settings = config.settings()
    page = ''.join(random.choice(string.printable) for i in range(bytes)) 
    char_count = 0 # Used to determine total number of usable characters
    char_values = '' # string of returend digets between 1 and 5
    index = [] # List of indexes of usable characters
    print(page)
   
    for position, letter in enumerate(page):
        if letter in ['1', '2', '3', '4', '5']:
            index.append(position) # Pulls indexes of char for later use
            char_values = char_values + str(letter)
            char_count = char_count + 1 # Increments character count 
            if settings.debug:
                print('Found ' + letter) # Prints which number was found
                print(char_count) # Prints current character count
    if settings.debug: print(char_values)
    return (index, char_values, page)