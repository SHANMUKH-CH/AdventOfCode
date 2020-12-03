# Right 3, down 1. (This is the slope you already checked.
# counting and multiplying the remaning trees
#!/usr/bin/env python3
import fileinput

formatted_INPUT = [l.rstrip('\n') for l in fileinput.input('day3_input.txt')]

rows, cols = len(formatted_INPUT), len(formatted_INPUT[0])
#rows = len of whole input file
#cols = number of columns in input file

def countingTress(down,right):
    row=tress=col=0
    while row < rows: #while not reached the bottom
        row += down
        col += right
        if row >= rows: break #if iterating rows greater than rows in file it break
        if formatted_INPUT[row][col % cols] == '#':
            '''
            col % cols
            if your column is bigger than totally number of columns in the input
            then you should take it`s modulus
            '''
            tress += 1
    return tress
if __name__=='__main__':
    print(
        countingTress(1,1)
        *countingTress(1,3)
        *countingTress(1,5)
        *countingTress(1,7)
        *countingTress(2,1)
    )