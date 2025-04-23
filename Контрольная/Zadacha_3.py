#Задача 3
print("\nЗадача 3")
def merge_tuples(tup1, tup2):
    combined = tup1 + tup2
    result = []
    for item in combined:
        if item not in result:
            result.append(item)
    return tuple(result)

tup1 = (1, 2, 3)
tup2 = (3, 4, 5)
print(merge_tuples(tup1, tup2))