import tkinter as tk
from tkinter import messagebox

group_names = ["Торопіна Поліна Всеволодівна", "Сіренко Ірина Дмітрівна", "Торопін Всеволод Миколайович"]

def check_login():
    user_name = entry.get()
    if user_name in group_names:
        messagebox.showinfo("Успішний вхід", "Ви успішно увійшли!")
        info = entry_info.get("1.0", "end-1c")
        with open("user_info.txt", "w") as file:
            file.write(info)
    else:
        messagebox.showwarning("Помилка", "Вас немає в базі даних. Що вам треба?")

root = tk.Tk()
root.title("Вхід")
root.geometry("300x200")

label = tk.Label(root, text="Введіть ваше ім'я:")
label.pack()

entry = tk.Entry(root)
entry.pack()

label_info = tk.Label(root, text="Введіть інформацію.Якщо можливо англійськіми літерами):")
label_info.pack()

entry_info = tk.Text(root, height=4)
entry_info.pack()

button = tk.Button(root, text="Увійти", command=check_login)
button.pack()

root.mainloop()
