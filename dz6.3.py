import os


def save_to_file(filename, text):
    file = open(filename, "w")
    file.write(text)
    file.close()


def read_from_file(filename):
    file = open(filename, "r")
    text = file.read()
    file.close()
    return text


filename = input("Введіть ім'я файла:")
text = input("Введіть текст для запису в файл:")
save_to_file(filename, text)
print(f"Текст який ви ввели для запису в файл {filename}: {read_from_file(filename)}")
