#Задание №10
students = (('Иван', 18, 75, 'Барнаул'),
            ('Антон', 18, 55, 'Новосибирск'),
            ('Андрей', 19, 80, 'Астана'),
            ('Владимир', 18, 45, 'Барнаул'),
            ('Валерий', 18, 70, 'Омск'),
            ('Пётр', 20, 30, 'Томск'),
            ('Марк', 17, 95, 'Кемерово')
)

def good_student(studs):
    grads = []
    names = []
    for i in studs:
        grads.append(i[2])
    average_grad = sum(grads) // len(grads)

    for i in studs:
        if i[2] >= average_grad:
            names.append(i[0])

    result = f"Ученики {names} в этом семестре хорошо учатся!"
    return result


print(good_student(students))

