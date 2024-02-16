import random


def add_random_symbol(text):
    symbols = "QWERTYUIOPASDFGHJKLZXCVBNM0123456789"
    symbols_cnt = len(symbols)
    random_symbol = symbols[random.randint(0, symbols_cnt)]
    random_position_number = random.randint(0, len(text))
    new_text = text[:random_position_number] + random_symbol + text[random_position_number:]
    return new_text


text = input("Введіть строку для вставки випадкового символа: ")
print(f"Строка з випадковим символом: {add_random_symbol(text)}")
