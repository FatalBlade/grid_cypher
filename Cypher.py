Debug = True
def create_cypher():
    """ This Function creates a one time Cypher from a given word """
    Cypher = { 11: 'a',  21: 'b',  31: 'c',  41: 'd',  51: 'e', 
               12: 'f',  22: 'g',  32: 'h',  42: 'i',  52: 'j/k',
               13: 'l',  23: 'm',  33: 'n',  43: 'o',  53: 'p',
               14: 'q',  24: 'r',  34: 's',  44: 't',  54: 'u',
               15: 'v',  25: 'w',  35: 'x',  45: 'y',  55: 'z' }
    Alpha = ['a', 'b', 'c', 'd', 'e',
            'f', 'g', 'h', 'i', 'j/k',
            'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']
    Key = []
    Axis = [11, 21, 31, 41, 51,
            12, 22, 32, 42, 52,
            13, 23, 33, 43, 53,
            14, 24, 34, 44, 54,
            15, 25, 35, 45, 55]
    selector = 0
    if Debug:
        print(Cypher[11], Cypher[13], Cypher[51], Cypher[35])
        print(Alpha)
    word = input('Chose a 5 letter word with no repeating letters or the letters j/k: ')
    wordLower = word.lower()
    if Debug:
        print(wordLower)
    
    for letter in wordLower:
            Alpha.remove(letter)
            
    if Debug:
        print(Alpha)
    
    for letter in wordLower:
            Key.append(letter)
    
    if Debug:
        print(Key)
    
    Final = Key + Alpha
    
    if Debug:
        print(Final)
    
    for key in Cypher:
        Cypher[Axis[selector]] = Final[selector]
        selector = selector +1
    if Debug:
        print(Cypher)
        
create_cypher()