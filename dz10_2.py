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


def auth_user(login, password):
    for student in get_students():
        if student.login == login and student.password == password:
            return student
    return None


input_login = input("Введіть логін: ")
input_password = input("Введіть пароль: ")
student = auth_user(input_login, input_password)
if student is None:
    print(f"Користувача з логіном {input_login} не знайдено, або невірний пароль")
else:
    print(f"Вітаю {student.firstname} {student.lastname} ви авторизовані!")
