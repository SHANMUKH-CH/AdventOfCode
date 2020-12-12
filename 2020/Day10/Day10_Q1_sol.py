#!/usr/bin/env python3
def _Q1(x):
    _one, _three = 0, 0
    for x, y in zip(x, x[1:]):
        if y-x == 1: _one +=1
        elif y-x == 3: _three += 1
    return (_one * _three)

if __name__ == '__main__':
    x = [int(l) for l in [l.rstrip('\n') for l in open('day10_input.txt','r')]]
    x.append(0)
    x.append(max(x)+3)
    x.sort()
    print(_Q1(x))