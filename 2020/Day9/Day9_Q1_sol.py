#!/usr/bin/env python3
def _Q1(l,e):
    for a in range(25,e):
        b = bool(0)
        for c in range(a - 25, a):
            for d in range(a - 25, a):
                if l[c] + l[d] == l[a]:
                    b = bool(1)
        if b == bool(0):
            z = l[a]
            return l[a]

if __name__=='__main__':
    # with open('day9_input') as i:
    #     l = i.read().splitlines()
    # l = [int(l) for l in l]
    x = list(map(int, open('day9_input.txt').read().splitlines()))
    y=len(x)
    print(_Q1(x,y))