import random

def random_number():
    # Користувач вводить найменше та найбільше значення
    smaller = int(input("Введіть найменше значення: "))
    bigger = int(input("Введіть найбільше значення: "))

    # Перевірка правильності введених значень
    if smaller >= bigger:
        print("Найменше значення повинно бути менше за найбільше.")
        return

    # Генерація випадкового числа у заданому діапазоні
    random_number = random.randint(smaller, bigger)

    # Виведення результату
    print("Ваше випадкове число:", random_number)

# Виклик функції
random_number()