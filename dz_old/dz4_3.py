import random

def random_name():
    names = input("Введіть назви, розділені пробілами: ").split()

    if not names:
        return "Список імен порожній."

    return random.choice(names)

result = random_name()
print(f"Випадкова назва: {result}")
