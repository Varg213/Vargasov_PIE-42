#Задача#1
print("Задача 1")
lat_letters = [
    (['A', 'E', 'I', 'O', 'U', 'L', 'N', 'S', 'T', 'R'], 1),
    (['D', 'G'], 2),
    (['B', 'C', 'M', 'P'], 3),
    (['F', 'H', 'V', 'W', 'Y'], 4),
    (['K'], 5),
    (['J', 'X'], 8),
    (['Q', 'Z'], 10)
]

lat_scores = {}
for letters, score in lat_letters:
    for letter in letters:
        lat_scores[letter] = score

cyr_letters = [
    (['А', 'В', 'Е', 'И', 'Н', 'О', 'Р', 'С', 'Т'], 1),
    (['Д', 'К', 'Л', 'М', 'П', 'У'], 2),
    (['Б', 'Г', 'Ё', 'Ь', 'Я'], 3),
    (['Й', 'Ы'], 4),
    (['Ж', 'З', 'Х', 'Ц', 'Ч'], 5),
    (['Ш', 'Э', 'Ю'], 8),
    (['Ф', 'Щ', 'Ъ'], 10)
]

cyr_scores = {}
for letters, score in cyr_letters:
    for letter in letters:
        cyr_scores[letter] = score

word = input("Введите слово: ").strip().upper()

if not word:
    print(0)
else:
    first_char = word[0]
    if first_char in lat_scores:
        scores = lat_scores
    elif first_char in cyr_scores:
        scores = cyr_scores
    else:
        print(0)
        exit()

    total = 0
    for char in word:
        total += scores.get(char, 0)
    print(f"Стоимость слова: {total}")

