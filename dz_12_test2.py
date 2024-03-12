import tkinter as tk
import random


class Game:
    def __init__(self, master, width, height):
        self.message_label = None
        self.login_button = None
        self.password_entry = None
        self.password_label = None
        self.username_entry = None
        self.username_label = None
        self.login_frame = None
        self.master = master
        self.width = width
        self.height = height
        self.master.title("Гра Clikcer-Bomber")
        self.users = {"Polina": "123", "Irina": "1234", "Vsevolod": "12345"}
        self.show_login_page()

    def show_login_page(self):
        self.login_frame = tk.Frame(self.master)
        self.login_frame.pack()

        self.username_label = tk.Label(self.login_frame, text="Ім'я користувача:")
        self.username_label.grid(row=0, column=0)
        self.username_entry = tk.Entry(self.login_frame)
        self.username_entry.grid(row=0, column=1)

        self.password_label = tk.Label(self.login_frame, text="Пароль:")
        self.password_label.grid(row=1, column=0)
        self.password_entry = tk.Entry(self.login_frame, show="*")
        self.password_entry.grid(row=1, column=1)

        self.login_button = tk.Button(self.login_frame, text="Авторизуватись", command=self.auth)
        self.login_button.grid(row=2, columnspan=2)

    def auth(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username in self.users:
            if self.users[username] == password:
                self.show_message("Ви авторизовані")
                self.show_game_menu_page()
            else:
                self.show_message("Невірний пароль")
        else:
            self.users[username] = password
            self.show_message("Створено аккаунт, та авторизовано")
            self.show_game_menu_page()

    def show_message(self, message):
        self.message_label = tk.Label(self.login_frame, text=message)
        self.message_label.grid(row=3, columnspan=2)

    def show_game_menu_page(self):
        self.login_frame.destroy()

        self.menu_frame = tk.Frame(self.master)
        self.menu_frame.pack()

        self.players_label = tk.Label(self.menu_frame, text="Введіть кількість гравців, максимум 3:")
        self.players_label.grid(row=0, column=0)
        self.players_entry = tk.Entry(self.menu_frame)
        self.players_entry.grid(row=0, column=1)

        self.steps_label = tk.Label(self.menu_frame, text="Кількість кроків, максимум 10:")
        self.steps_label.grid(row=1, column=0)
        self.steps_entry = tk.Entry(self.menu_frame)
        self.steps_entry.grid(row=1, column=1)

        self.start_button = tk.Button(self.menu_frame, text="Початок гри", command=self.game_start)
        self.start_button.grid(row=2, columnspan=2)

    def game_start(self):
        num_players = int(self.players_entry.get())
        num_steps = int(self.steps_entry.get())

        self.menu_frame.destroy()

        self.game_frame = tk.Frame(self.master)
        self.game_frame.pack()

        self.players = []

        for i in range(num_players):
            player = Player(self.master, i, num_steps, self.game_end, self.width, self.height)
            self.players.append(player)

        self.winner_label = tk.Label(self.master, text="")
        self.winner_label.pack()

    def game_end(self):
        max_moves = 0
        winner = None
        for player in self.players:
            print(player.name)
            if player.num_steps >= max_moves:
                max_moves = player.num_steps
                winner = player.name

        self.winner_label.config(text=f"Переможець: {winner}")


class Player:
    def __init__(self, master, player_num, num_steps, result_callback, width, height):
        self.width = width
        self.height = height
        self.master = master
        self.palyer_num = player_num
        self.name = f"Гравець {player_num + 1}"
        self.num_steps = num_steps
        self.end_game_callback = result_callback

        self.position_x = random.randint(0, self.width - 50)
        self.position_y = random.randint(0, self.height - 50)

        # self.square = tk.Label(self.master, text=self.name)
        self.square = tk.Frame(self.master, width=50, height=50)
        self.square.place(x=self.position_x, y=self.position_y)
        self.bg = "yellow"
        if player_num == 1: self.bg = "green"
        if player_num == 2: self.bg = "cyan"
        self.name_label = tk.Label(self.square, text=self.name, bg=self.bg, height=3)
        self.name_label.pack(expand=True, fill="both")
        self.name_label.bind("<Button-1>", self.move_square)

        self.steps_label = tk.Label(self.master, text=f"Залишилось кроків: {self.num_steps}")
        self.steps_label.place(x=0, y=20)

    def move_square(self, event):
        print(self.num_steps)
        if self.num_steps > 0:
            self.position_x = random.randint(0, self.width - 50)
            self.position_y = random.randint(0, self.height - 50)
            self.square.place(x=self.position_x, y=self.position_y)
            self.num_steps -= 1
            self.steps_label.config(text=f"Залишилось кроків: {self.num_steps}")
        if self.num_steps == 0:
            self.square.unbind("<Button-1>")
            self.end_game_callback()


root = tk.Tk()
screen_width = 800
screen_height = 600
root.geometry(f"{screen_width}x{screen_height}")
game = Game(root, screen_width, screen_height)
root.mainloop()
