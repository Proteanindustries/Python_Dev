def of_age():
    is_of_age = int(age) >18

def is_licensed():
    is_licensed == True

def drivercheck(is_of_age = 0, is_licensed = False):
    if is_of_age > 18 and is_licensed == True:
        print('You are old enough and are licensed to drive!')
    elif is_of_age < 18 and is_licensed == False:
        print('You are not old enough or not licensed to drive!')
    elif is_of_age > 18 and is_licensed == False:
        print('You are not licensed to drive!')
    else:
        print('Find an older, licensed driver.')
    print('Safety First!')

drivercheck(19,True)
drivercheck(25, False)
drivercheck(15, False)
