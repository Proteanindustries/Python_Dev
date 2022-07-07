is_of_age = True
is_licensed = True

if is_of_age == True and is_licensed ==True :
    print('You are old enough and are licensed to drive!')
elif is_of_age == False and is_licensed == False:
    print('You are not old enough or not licensed to drive!')
elif is_of_age == True and is_licensed == False:
    print('You are not licensed to drive!')
else:
    print('Find an older, licensed driver.')

print('Safety First, Enjoy Your Ride!')
