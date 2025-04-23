#Задание №6
C = (3, 's', 1, 5, 's')
count = 0
print(len(C))
for i in C:
    if i == 's':
        count += 1
print(count)
for i in C:
    if i == 's':
        print(C.index(i))
        break

