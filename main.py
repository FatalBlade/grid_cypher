import Cypher
import Page
import settings

# Initialize settings
settings = settings.settings()

cypher = Cypher.create_cypher()
print('\n')
bytess = input('How many bytes do you need? ')
print('\n')
index, char_values, page = Page.create_page(int(bytess))
print(char_values) # Temporary placeholder
print(page) # Temporary placeholder
print(index) # Temporary placeholder
message = Cypher.encrypt(cypher, index)
print('\n')
print(message)
print('\n')

"""
encrypt(cypher, index):

replace():

decrypt():

"""