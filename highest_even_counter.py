my_list = [10, 2, 3, 4, 6, 8, 21]

def highest_even(li):
    new_list = []
    for item in li:
        if item % 2 == 0:
            new_list.append(item)
    return max(new_list)


print(highest_even(my_list))
