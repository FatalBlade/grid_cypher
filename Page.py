# Page.py

import random
import string
import settings

char = [] # List of usable digits
char_test = ''

def create_page(bytes):
    """ This function creates the page  """
    letters_and_digits = string.ascii_letters + string.digits + string.punctuation
    page = ''.join(random.choice(letters_and_digits) for i in range(bytes)) 
    char_count = 0 # Used to determine total number of usable characters
    global char_test
    print(page)
    for letter in page:
        if letter == 1:
            char.append(letter) # Adds digit to usuable list
            char_test = char_test + str(letter)
            char_count = char_count + 1 # Increments character count 
            if settings.debug:
                print('Found 1') # Prints which number was found
                print(char_count) # Prints current character count
        if letter == 2:
            char.append(letter)
            char_test = char_test + str(letter)
            char_count = char_count + 1
            if settings.debug:
                print('Found 2')
                print(char_count)
        if letter == 3:
            char.append(letter)
            char_test = char_test + str(letter)
            char_count = char_count + 1
            if settings.debug:
                print('Found 3')
                print(char_count)
        if letter == 4:
            char.append(letter)
            char_test = char_test + str(letter)
            char_count = char_count + 1
            if settings.debug:
                print('Found 4')
                print(char_count)
        if letter == 5:
            char.append(letter)
            char_test = char_test + str(letter)
            char_count = char_count + 1
            if settings.debug:
                print('Found 5')
                print(char_count)
        else:
            continue
    print(char)
    print(char_test)

    
    



