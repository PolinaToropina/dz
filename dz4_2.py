import random

users = []
heroes = ['Iron Man', 'Batman', 'Superman', 'Thor', 'Hulk', 'Flash']

def assign_hero(name):
    if heroes:
        hero = random.choice(heroes)
        heroes.remove(hero)
        return hero
    else:
        return "Немає більше вільних героїв"

while heroes:
    while True:
        name = input("Введіть ваше ім'я: ")
        if name:
            break
        else: name = input("Ви не ввели значення, введіть ваше ім'я: ")

    hero = assign_hero(name)
    users.append((name, hero))
print("\nКористувачі та їхні супергерої:")
for user in users:
    print(f"{user[0]} - {user[1]}")