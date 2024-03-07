import tkinter as tk
from tkinter import messagebox

class Students:
    def __init__(self, login, password, firstname, lastname):
        self.login = login
        self.password = password
        self.firstname = firstname
        self.lastname = lastname


def get_students():
    students = [
        Students("Polina", "123", "Поліна", "Торопіна"),
        Students("Irina", "1234", "Ірина", "Сіренко"),
        Students("Vsevolod", "12345", "Всеволод", "Торопін")
    ]
    return students


def auth_user():
    login = login_entry.get()
    password = password_entry.get()

    for student in get_students():
        if student.login == login and student.password == password:
            messagebox.showinfo("Успішно!", f"Вітаємо, {student.firstname} {student.lastname}!")
            return
    messagebox.showerror("Помилка", "Невірно введені дані")

root = tk.Tk()
root.title("Авторизація студента")

login_label = tk.Label(root, text="Логін:")
login_label.grid(row=0, column=0, padx=10, pady=5)
login_entry = tk.Entry(root)
login_entry.grid(row=0, column=1, padx=10, pady=5)

password_label = tk.Label(root, text="Пароль:")
password_label.grid(row=1, column=0, padx=10, pady=5)
password_entry = tk.Entry(root, show="*")
password_entry.grid(row=1, column=1, padx=10, pady=5)

auth_button = tk.Button(root, text="Авторизуватися", command=auth_user)
auth_button.grid(row=2, column=0, columnspan=2, pady=10)

root.mainloop()

input_login = input("Введіть логін: ")
input_password = input("Введіть пароль: ")
student = auth_user(input_login, input_password)
if student is None:
    print(f"Користувача з логіном {input_login} не знайдено, або невірний пароль")
else:
    print(f"Вітаю {student.firstname} {student.lastname} ви авторизовані!")
