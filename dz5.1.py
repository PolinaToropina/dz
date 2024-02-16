def corrector(str, width, symbol):
    if len(str) >= width:
        return str
    left_spaces = (width - len(str)) // 2
    right_spaces = width - len(str) - left_spaces
    return symbol * left_spaces + str + fill_char * right_spaces

str = input("Введіть строку")
width = input("Введіть довжину нової строки")
fill_char = input("Введіть символ, який буде використаний для заповнення пробілів")
result = corrector(str, int(width), fill_char)
print(result)
