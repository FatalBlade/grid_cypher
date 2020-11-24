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
index, char_values, page, char_count = Page.create_page(int(bytess))
print(char_values)
print(page)
print(index)
encrypted = Cypher.encrypt(cypher, index, char_count)
print('\n')
print(encrypted)
print('\n')
#print(Cypher.get_key(cypher, 'f'))
decrypted = Cypher.decrypt(cypher, encrypted)
print(decrypted)


"""

replace():


"""
