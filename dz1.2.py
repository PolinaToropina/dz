def рисування_зірки(довжина_сторони):
    for string in range(довжина_сторони):
        рядок_зірок = '*' * довжина_сторони
        print(рядок_зірок)

# Користувач вводить довжину сторони
length = int(input("Введіть довжину сторони для зірки: "))

# Виклик функції для рисування зірки
рисування_зірки(length)