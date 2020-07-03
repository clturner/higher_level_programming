#!/usr/bin/python3
letter = 97

while(letter < 123):
    if letter == 101 or letter == 113:
        letter += 1
    else:
        print('{}'.format(chr(letter)), end="")
        letter = letter + 1
