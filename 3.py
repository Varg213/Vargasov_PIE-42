#Задание №3
natnum_list = [1, 1, 1, 1, 1, 1, 1]
natnum_list_2 = [1, 2, 3, 4, 5, 7, 7]
natnum_list_3 = [1, 1, 1, 4, 5, 6, 1]

def set_gen(list):
    list_to_set = []
    rep = 2
    for i in list:
        if list.count(i) > 1:
            list_to_set.append(i)
            list_to_set.append(str(i) * rep)
            rep += 1
        else:
            list_to_set.append(i)

    return set(list_to_set)

print(set_gen(natnum_list))
print(set_gen(natnum_list_2))
print(set_gen(natnum_list_3))