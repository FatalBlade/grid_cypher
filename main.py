from Cypher import create_cypher
from Page import create_page
import settings

# Initialize settings
settings.init() 

create_cypher()
print('\n')
bytess = input('How many bytes do you need? ')
print('\n')
create_page(int(bytess))
#print(char_test)