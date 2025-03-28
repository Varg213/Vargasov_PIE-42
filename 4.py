#Задание №4
set_1 = {1, 2, 3, 4}
set_2 = {1, 2}
set_3 = {4, 3, 2, 1}
set_4 = {5, 6}

def superset(set1, set2):

    if set1 > set2:
        print(f'Объект {set1} является чистым супермножеством')
    elif set1 == set2:
        print(f'Множества равны')
    elif set1 < set2:
        print(f'Объект {set2} является чистым супермножеством')
    else:
        print('Супермножество не обнаружено')

superset(set_1, set_2)
superset(set_1, set_3)
superset(set_2, set_3)
superset(set_4, set_2)