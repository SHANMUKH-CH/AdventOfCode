def _Q2(listOfnumbers, limit):
    dict = {x: i for i, x in enumerate(listOfnumbers[:-1])}
    number = listOfnumbers[-1]
    for x in range(len(listOfnumbers), limit):
        if number in dict: NEW = x - dict[number] - 1
        else: NEW = 0
        dict[number] = x-1
        number = NEW
    return number
if __name__ == '__main__':
    print(_Q2([1,2,16,19,18,0],30000000))