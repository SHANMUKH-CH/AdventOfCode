from termcolor import colored
#Find the two entries that sum to 2020!
#what do you get if you multiply them together?
def _Q1(n):
    for A_num in set(n):
        #checking two numbers which has sum = 2020
        if (_2nd_number := 2020 - A_num) in set(n):
            #wulavrus operator: assignment expression
            #to know more about wulavrus operator
            #https://github.com/SHANMUKH-CH/pythonPrograms/blob/main/tricks%20and%20tips/walrus%20operator.py
            return (colored(f'by usual way {A_num * _2nd_number}','blue'))
#q1 solution 2 using itertools and combinations
import itertools

def _Q1_iterway(n):
    lol = [ x * y for x, y in itertools.combinations(map(int, n), 2) if x + y  == 2020]
    print(colored(f'using itertools {lol[0]}','red'))
    
if __name__=='__main__':
    with open('my_input.txt') as f:
        numbers_in_file = list(sorted(map(int,f)))
        print(_Q1(numbers_in_file))
        _Q1_iterway(numbers_in_file)