def counting_valid_fields(x):
    return(sum(1 if all(fields in passwords for fields in ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']) else 0 for passwords in x))

if __name__=='__main__':
    _formated_input = [x.rstrip('\n') for x in open('day4_input.txt').read().split('\n\n')]
    print(counting_valid_fields(_formated_input))