import os

def print_file_tree(path, pad=""):
        items = os.listdir(path)
        for i, item in enumerate(items):
            item_path = os.path.join(path, item)
            if os.path.isdir(item_path):
                print(pad + "" + item + ":")
                print_file_tree(item_path, pad + "\t")
            else:
                print(pad + "" + item)


directory_path = input("Введіть шлях до директорії:")
print("деревоподібна структура файлів і директорій:")
print_file_tree(directory_path)
