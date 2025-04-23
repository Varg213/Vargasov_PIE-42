#Задача 4
print("\nЗадача 4")
data = [
    ("Москва", 2020, 12_000_000),
    ("Санкт-Петербург", 2020, 5_400_000),
    ("Москва", 2021, 12_200_000),
    ("Санкт-Петербург", 2021, 5_350_000)
]

city_population = {}

for city, year, population in data:
    if city in city_population:
        city_population[city] += population
    else:
        city_population[city] = population

for city, total in city_population.items():
    print(f"{city}: {total}")