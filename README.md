# grid_cypher
simple gird cypher from a code word along with a randomly generated page to encrypt/decrypt messages


This program is intended to do a few different things

When given a word that meets the correct criteria it will create a simple 5x5 grid cypher

It will generate a page of random characters using os.urandom
    This will be our one time page style whitenoise page
    
From there the program will pull the usable characters and use the already created cypher to replaec them with the encrypted text

The program will also be able to take that page and recreate the cyper with the given code word to decrypt the mesage
