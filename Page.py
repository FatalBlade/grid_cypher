from os import urandom
import settings

page = urandom(262144) 
char = 0 # Used to determine total number of usable characters

print(page)

for letter in page:
    
    if letter == 1:
        print('Found 1') # Temporary placeholder
        # Increments character count
        char = char + 1
        if settings.debug:
            # Prints current character count
            print(char)
    if letter == 2:
        print('Found 2') # Temporary placeholder
        # Increments character count
        char = char + 1
        if settings.debug:
            # Prints current character count
            print(char)
    if letter == 3:
        print('Found 3') # Temporary placeholder
        # Increments character count
        char = char + 1
        if settings.debug:
            # Prints current character count
            print(char)
    if letter == 4:
        print('Found 4') # Temporary placeholder
        # Increments character count
        char = char + 1
        if settings.debug:
            # Prints current character count
            print(char)
    if letter == 5:
        print('Found 5') # Temporary placeholder
        # Increments character count
        char = char + 1
        if settings.debug:
            # Prints current character count
            print(char)
    else:
        continue