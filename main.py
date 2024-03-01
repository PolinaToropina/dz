import re
import tkinter as tk

def validate_credentials():
    login = login_entry.get()
    password = password_entry.get()

root = tk.Tk()
root.geometry("1000x500+700+500")
root.resizable(False, False)

login_pattern = re.compile(r"^\w{3,16}@[a-z]{3,10}\.[a-z]{3,10}")
password_pattern = re.compile(r"^\w{8,16}$")

login_label = tk.Label(root, text='Логін', padx=50)
login_entry = tk.Entry(root, width=20)

password_label = tk.Label(root, text='Пароль', padx=50)
password_entry = tk.Entry(root, width=20, show='*')

authorize_button = tk.Button(root, text='Авторизація')

root.grid_columnconfigure(0, minsize=150)
root.grid_columnconfigure(1, minsize=250)
root.grid_rowconfigure(0, minsize=90)
root.grid_rowconfigure(1, minsize=90)

login_label.grid(column=0, row=0)
login_entry.grid(column=1, row=0)

password_label.grid(column=0, row=1)
password_entry.grid(column=1, row=1)

authorize_button.grid(column=1, row=2, pady=10)

root.mainloop()
