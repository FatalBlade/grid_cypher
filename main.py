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
page_final = Page.replace(page, index, encrypted)
print(decrypted)
print('\n')
print(page)
# SJ asked for a seperater so I gave him a seperater
print('8=====================D')
print(page_final)
print('\n')
print(Page.pull_page(page_final))
_, pull_values, _, _ = Page.pull_page(page_final)
print(Cypher.decrypt(cypher, pull_values))

