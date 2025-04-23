#Задание №9
def slice(collection, element):
    try:
        start_index = collection.index(element)
        end_index = collection.index(element, start_index + 1)
        return collection[start_index:end_index + 1]
    except ValueError:
        return []
    except IndexError:
        return collection[start_index:]

# Пример использования
my_list = [1, 2, 3, 4, 2, 5]
result = slice(my_list, 2)
print(result)

