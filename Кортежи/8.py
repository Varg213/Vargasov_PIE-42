#Задание №8
def tpl_sort(tuple):
    check = None

    for i in tuple:
        if type(i) is int:
            check = True
        else:
            check = False

    if check == True:
        return sorted(tuple)
    elif check == False:
        return tuple

C_1 = (3, 4, 1, 2, 6, 5)
C_2 = (1, 3, 2, 2.0)
C_3 = (1, 3, 2, 'str')

print(tpl_sort(C_1))
print(tpl_sort(C_2))
print(tpl_sort(C_3))



