# settings.py

class settings():

    def __init__(self):
        # DO NOT CHANGE // Controls the x/y AXIS' of the cypher
        self.AXIS = [11, 21, 31, 41, 51,
                     12, 22, 32, 42, 52,
                     13, 23, 33, 43, 53,
                     14, 24, 34, 44, 54,
                     15, 25, 35, 45, 55]
        # This is the actual cypher itself at it's default a-z settings
        self.cypher = {11: 'a', 21: 'b', 31: 'c', 41: 'd', 51: 'e', 
                       12: 'f', 22: 'g', 32: 'h', 42: 'i', 52: 'j/k',
                       13: 'l', 23: 'm', 33: 'n', 43: 'o', 53: 'p',
                       14: 'q', 24: 'r', 34: 's', 44: 't', 54: 'u',
                       15: 'v', 25: 'w', 35: 'x', 45: 'y', 55: 'z'}
        # Default ordered list a-z
        self.alpha = ['a', 'b', 'c', 'd', 'e',
                      'f', 'g', 'h', 'i', 'j/k',
                      'l', 'm', 'n', 'o', 'p',
                      'q', 'r', 's', 't', 'u',
                      'v', 'w', 'x', 'y', 'z']
        self.debug = True
        