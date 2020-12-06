def _Q1(x):
    '''
    list comp: https://github.com/SHANMUKH-CH/pythonPrograms/blob/main/tricks%20and%20tips/list%20comprehension.py
    '''
    return(sum([len(a) for a in [set(elements.replace('\n','')) for elements in x]]))

if __name__ =='__main__':
    formatted_INPUT = [x.rstrip('\n') for x in open('day6_input.txt','r').read().split('\n\n')]
    print(_Q1(formatted_INPUT))