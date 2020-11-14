# Page.py

import random
import string
import settings

char = [] # List of usable digits
char_test = ''

def create_page(bytes):
    """ This function creates the page  """
    page = ''.join(random.choice(string.printable) for i in range(bytes)) 
    char_count = 0 # Used to determine total number of usable characters
    global char_test
    print(page)
    for letter in page:
        if letter in ['1', '2', '3', '4', '5']:
            char.append(letter) # Adds digit to usuable list
            char_test = char_test + str(letter)
            char_count = char_count + 1 # Increments character count 
            if settings.debug:
                print('Found ' + letter) # Prints which number was found
                print(char_count) # Prints current character count
    print(char)
    print(char_test)
