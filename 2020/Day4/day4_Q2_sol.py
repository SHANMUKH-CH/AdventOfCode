import re
ecl = set(['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'])
'''
lambda tutorial
https://github.com/SHANMUKH-CH/pythonPrograms/blob/main/tricks%20and%20tips/lambda%20function.py
'''
validF = {
    'byr': lambda S: 1920 <= int(S) <= 2002,
    'iyr': lambda S: 2010 <= int(S) <= 2020,
    'eyr': lambda S: 2020 <= int(S) <= 2030,
    'hgt': lambda S: S[-2:] == 'cm' and 150 <= int(S[:-2]) <= 193 or S[-2:] == 'in' and 59 <= int(S[:-2]) <= 76,
    'hcl': lambda S: bool(re.fullmatch('^#[a-f0-9]{6}$', S)),
    'ecl': lambda S: S in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'],
    'pid': lambda S: bool(re.fullmatch('^[0-9]{9}$', S))}

def _valid_fields(p):    
    return (all(f in p for f in validF.keys()) and all(validF[f](p[f]) for f in validF.keys()))

if __name__ == '__main__':
    _formated_input = [x.rstrip('\n') for x in open('day4_input.txt').read().split('\n\n')]
    passports = [dict(f.split(':') for f in x.split('\n')) for x in [x.replace(' ', '\n') for x in _formated_input]]
    print(sum(_valid_fields(x) for x in passports))