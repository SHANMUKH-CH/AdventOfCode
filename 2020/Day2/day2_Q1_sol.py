import re
def _Q2(x):
    """
    In input argument there are three elements 1.atleast 2.atmost 3.password
    """
    return sum(atleast <= sum(password) <=atmost for atleast, atmost, password in x)
if __name__=='__main__':
    #using regular experssions remove 
    _listOf3 = [re.split('[: \-]', elements.strip()) for elements in open('day2_input.txt')]
    #printing the splited list
    #print(_listOf3)
    #assigining the _listOf3 to atleast, atmost, character, password
    #checking the characters(atmost, atleast) in existing password storing it in tuple
    x = [(int(atleast), int(atmost), [y == character for y in password]) for atleast, atmost, character, _, password in _listOf3]
    print(_Q2(x))
