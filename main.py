import Cypher
import Page
import settings

""" All current commits on this page are for testing purposes 
    and are completely temporary """

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
encrypted = Cypher.encrypt(cypher, index)
print('\n')
print(encrypted)
print('\n')
#print(Cypher.get_key(cypher, 'f'))

"""

replace():

decrypt():

"""
