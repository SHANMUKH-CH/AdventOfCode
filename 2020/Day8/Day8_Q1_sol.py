#!/usr/bin/env python3
def _Q1(line):
    x, i, crap_i_saw= 0, 0, set()
    while i not in crap_i_saw:
        crap_i_saw.add(i); O, num = line[i]
        if O =='nop': i += 1; continue
        elif O == 'jmp': i += int(num)
        elif O == 'acc': i += 1; x+=int(num)
    return (x)

if __name__=='__main__':    
    with open('day8_input.txt') as x:
        y = [line.split() for line in  x.read().split("\n")]
        print(_Q1(y))