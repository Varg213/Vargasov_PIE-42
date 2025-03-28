#Задание №2
dict_1 = {1: 12, 2: 33, 3: 10, 4: 10, 5: 2, 6: 90}
dict_2 = {1: 12, 3: 7, 4: 1, 5: 2, 7: 112}
dict_3 = {2: 3, 3: 3, 4: 60, 6: 8, 7: 25, 8: 71}
dict_4 = {3: 1, 4: 13, 5: 31, 9: 9, 10: 556}

def max_dict(d_1, d_2, d_3, d_4):
    dict_5 = {}
    all_keys = set(d_1.keys()).union(d_2.keys(), d_3.keys(), d_4.keys())
    for key in all_keys:
        value_1 = d_1.get(key, float('-inf'))
        value_2 = d_2.get(key, float('-inf'))
        value_3 = d_3.get(key, float('-inf'))
        value_4 = d_4.get(key, float('-inf'))
        dict_5[key] = max(value_1, value_2, value_3, value_4)

    print(dict_5)

max_dict(dict_1, dict_2, dict_3, dict_4)

def sum_dict(d_1, d_2, d_3, d_4):
    dict_5 = {}

    for d in (d_1, d_2, d_3, d_4):
        for key, value in d.items():
            if key in dict_5:
                dict_5[key] += value
            else:
                dict_5[key] = value

    print(dict_5)

sum_dict(dict_1, dict_2, dict_3, dict_4)