from itertools import count
def _Q1(_1st, bu):
    return(next((t - _1st)*b
            for t in count(_1st) for b in bu
            if t % b == 0))

if __name__ =='__main__':
    with open('day13_input.txt','r') as x:
        x = [x.strip() for x in x.readlines()]
    _1st = int(x[0])
    b_times = [(-i, int(x)) for i, x in enumerate(x[1].split(',')) if x != 'x']
    #unpacking tuples check my python tricks and tips subdir in pythonprogram repo
    _, bu = zip(*b_times)
    print(_Q1(_1st, bu))