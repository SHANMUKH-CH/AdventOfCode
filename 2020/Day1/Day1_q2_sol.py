from termcolor import colored
import itertools
'''
https://docs.python.org/3/library/itertools.html#module-itertools
itertools.combinations(iterable, r): Return r length subsequences of elements from the input iterable.
'''
def _Q2(n):
    lol = [x*y*z for x, y, z in itertools.combinations(map(int, n), 3) if x + y + z == 2020]
    print(colored((lol[0]),'blue'))
          
if __name__=='__main__':
    with open('my_input.txt') as f:
        numbers_in_file = list(sorted(map(int,f)))
        _Q2(numbers_in_file)