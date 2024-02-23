import os
from shutil import copy

def copy_images(source_dir, destination_dir):
    if not os.path.exists(source_dir):
        print(f"Директорії {source_dir} не існує.")
        return
    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)

    for filename in os.listdir(source_dir):
        source_path = os.path.join(source_dir, filename)
        if filename.lower().endswith(('.png', '.jpg', '.bmp')):
            copy(source_path, destination_dir)
            print(f"Скопійовано: {filename}")

source_directory = input("Введіть шлях до директорії з зображеннями: ")
destination_directory = input("Введіть шлях до цільової директорії: ")

copy_images(source_directory, destination_directory)
