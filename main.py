from Cypher import create_cypher
import Page
import settings

# Initialize settings
settings.init() 

create_cypher()
print('\n')
bytess = input('How many bytes do you need? ')
print('\n')
index, char_test, page = Page.create_page(int(bytess))
print(char_test) # Temporary placeholder
print(page) # Temporary placeholder
print(index) # Temp[orary placeholder