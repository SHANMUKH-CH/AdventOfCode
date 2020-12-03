#!/usr/bin/env python3
import fileinput

formatted_INPUT = [x.rstrip('\n') for x in fileinput.input('day3_input.txt')]

rows, cols = len(formatted_INPUT), len(formatted_INPUT[0])
#rows = len of whole input file
#cols = number of columns in input file

def countingTress():
    row=tress=col=0
    while row < rows: #while not reached the bottom
        row += 1
        col += 3
        if row >= rows: break #if iterating rows greater than rows in file it break
        if formatted_INPUT[row][col % cols] == '#':
            '''
            col % cols
            if your column is bigger than totally number of columns in the input
            then you should take it`s modulus
            '''
            tress += 1
    return tress
print(countingTress())