import tkinter as tk
import random
from tkinter import Tk


class Player:
    def __init__(self, name, clicks):
        self.name = name
        self.clicks = clicks
        self.moves = 0

def move_player(player):
    player.moves += 1
    player.clicks -= 1

def check_winner(players):
    winner = max(players, key=lambda x: x.moves)
    return winner

def login(username, password):


def start_game(num_players, num_steps):
    login_window: Tk = tk.Tk()
    login_window.title("Авторизація")
    username_label = tk.Label(login_window, text="Ім'я користувача:")
    username_entry = tk.Entry(login_window)
    password_label = tk.Label(login_window, text="Пароль:")
    password_entry = tk.Entry(login_window, show="*")
    login_button = tk.Button(login_window, text="Увійти", command=lambda: login(username_entry.get(), password_entry.get()))

    username_label.pack()
    username_entry.pack()
    password_label.pack()
    password_entry.pack()
    login_button.pack()

    login_window.mainloop()


def game_menu():
    menu_window = tk.Toplevel()
    menu_window.title("Меню гри")

    num_players_label = tk.Label(menu_window, text="Кількість гравців (максимум 3):")
    num_players_entry = tk.Entry(menu_window)
    num_steps_label = tk.Label(menu_window, text="Кількість кроків (максимум 10):")
    num_steps_entry = tk.Entry(menu_window)
    start_button = tk.Button(menu_window, text="Почати гру",
                             command=lambda: start_game(int(num_players_entry.get()), int(num_steps_entry.get())))

    num_players_label.pack()
    num_players_entry.pack()
    num_steps_label.pack()
    num_steps_entry.pack()
    start_button.pack()


def start_game(num_players, num_steps):

    pass


game_menu()

