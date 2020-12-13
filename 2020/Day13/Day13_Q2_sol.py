from itertools import count
from sympy.ntheory.modular import solve_congruence
#https://brilliant.org/wiki/chinese-remainder-theorem/
def _Q2(b):
    return solve_congruence(*b)[0]

if __name__ == '__main__':
    with open('day13_input.txt','r') as x:
        x = [x.strip() for x in x.readlines()]
    _1st = int(x[0])
    b_times = [(-i, int(x)) for i, x in enumerate(x[1].split(',')) if x != 'x']
    #unpacking tuples check my python tricks and tips subdir in pythonprogram repo
    print(_Q2(b_times))