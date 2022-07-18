# Page.py

import random
import string
import settings as config




def create_page(bytes):
    """ This function creates the one time page  """
    page = ''.join(random.choice(string.printable) for i in range(bytes)) 
    print(page)
    return pull_page(page)
   
def pull_page(page):
    settings = config.settings()
    char_count = 0 # Used to determine total number of usable characters
    char_values = '' # string of returend digets between 1 and 5
    index = [] # List of indexes of usable characters
    for position, letter in enumerate(page):
        if letter in ['1', '2', '3', '4', '5']:
            # Pulls indexes of char for later use
            index.append(position)
            # Adds found number to list
            char_values = char_values + str(letter)
            # Increments character count
            char_count = char_count + 1 
            if settings.debug:
                # Prints which number was found
                print('Found a ' + letter)
                # Prints current character count
                print(str(char_count) + ' usable characters')
    if settings.debug: print('List of values: ' + str(char_values))
    return (index, char_values, page, char_count)
    
def replace(page, index, encrypted):
    """ This function will replace available characters with our encrypted message """
    ls_page = list(page)
    for n in range(0, len(encrypted)):
        ls_page[index[n]] = encrypted[n]
    page_final = "".join(ls_page)
    return page_final
