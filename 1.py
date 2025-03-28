#Задание №1
dict_1 = {1: 'a', 2: 'b'}
dict_2 = {2: 'c', 4: 'd'}
dict_copy = dict_1.copy()
dict_copy.update(dict_2)
print(f"Объединение двух словарей первым способом: {dict_copy}")

dict_3 = dict_1 | dict_2
print(f"Объединение двух словарей вторым способом: {dict_3}")