# Page.py

import random
import string
import settings

char_test = ''
index = []

def create_page(bytes):
    """ This function creates the page  """
    page = ''.join(random.choice(string.printable) for i in range(bytes)) 
    char_count = 0 # Used to determine total number of usable characters
    global char_test
    global index
    print(page)
   
    for position, letter in enumerate(page):
        if letter in ['1', '2', '3', '4', '5']:
            index.append(position)
            char_test = char_test + str(letter)
            char_count = char_count + 1 # Increments character count 
            if settings.debug:
                print('Found ' + letter) # Prints which number was found
                print(char_count) # Prints current character count
    if settings.debug: print(char_test)
    return (index, char_test, page)