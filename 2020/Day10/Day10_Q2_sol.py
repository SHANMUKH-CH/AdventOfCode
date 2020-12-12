#!/usr/bin/env python3
def _Q2(n):
    x, y, z = 0, 0, 1
    for i in range(1, _peak + 1):
        if i in n: x, y, z = y, z, x + y + z
        else: x, y, z = y, z, 0
    print(z)
if __name__ == '__main__':
    x = [int(l) for l in [l.rstrip('\n') for l in open('day10_input.txt','r')]]
    _peak = max(x) + 3
    n = set(x)
    n.add(_peak)
    _Q2(n)