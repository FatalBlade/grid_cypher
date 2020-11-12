from os import urandom

page = urandom(262144)
char = 0
Debug = True

print(page)

for letter in page:
    
    if letter == 1:
        print('Found 1')
        char = char + 1
        if Debug:
            print(char)
    if letter == 2:
        print('Found 2')
        char = char + 1
        if Debug:
            print(char)
    if letter == 3:
        print('Found 3')
        char = char + 1
        if Debug:
            print(char)
    if letter == 4:
        print('Found 4')
        char = char + 1
        if Debug:
            print(char)
    if letter == 5:
        print('Found 5')
        char = char + 1
        if Debug:
            print(char)
    else:
        continue