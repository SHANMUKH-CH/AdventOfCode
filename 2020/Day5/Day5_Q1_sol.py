#!/usr/bin/env python3
import fileinput
def i(file):
    
    return {int(X.replace("B", "1").replace("F", "0").replace("R", "1").replace("L", "0"), 2) for X in file}

if __name__=='__main__':
    
    formatted_INPUT = [l.rstrip('\n') for l in fileinput.input('day5_input.txt')]
    
    print(max(i(formatted_INPUT)))