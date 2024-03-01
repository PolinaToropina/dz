group_names = ["Поліна", "Ірина", "Всеволод"]

def check_login(name):
    if name in group_names:
        print("Ви успішно увійшли!")
    else:
        print("Вас немає в базі даних. Що вам треба?")


    if name in group_names:
        input("Інформація:")
        print("Інформація збережена")


user_name = input("Введіть ваше ім'я: ")

check_login(user_name)
