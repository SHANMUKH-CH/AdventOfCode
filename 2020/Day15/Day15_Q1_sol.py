def _Q1(listOfnumbers, limit):
    dict = {x: i for i, x in enumerate(listOfnumbers[:-1])}
    number = listOfnumbers[-1]
    for x in range(len(listOfnumbers), limit):
        if number in dict: NEW = x - dict[number] - 1
        else: NEW = 0
        dict[number] = x-1
        number = NEW
    return number
if __name__ == '__main__':
    print(_Q1([1,2,16,19,18,0],2020))
# Is it starting to rain?
# Did the check bounce?
# Are we out of coffee?
# Is this going to hurt?
# Could you lose your job?
# Did the glass break?
# Was the baggage misrouted?
# Will this go on my record?
# Are you missing much money?
# Was anyone injured?
# Is the traffic heavy?
# Do I have to remove my clothes?
# Will it leave a scar?
# Must you go?
# Will this be in the papers?
# Is my time up already?
# Are we seeing the understudy?
# Will it affect my eyesight?
# Did all the books burn?
# Are you still smoking?
# Is the bone broken?
# Will I have to put him to sleep?
# Was the car totaled?
# Am I responsible for these charges?
# Are you contagious?
# Will we have to wait long?
# Is the runway icy?
# Was the gun loaded?
# Could this cause side effects?
# Do you know who betrayed you?
# Is the wound infected?
# Are we lost?
# Will it get any worse?