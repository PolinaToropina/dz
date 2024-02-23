import datetime


def get_day_of_week(month, day, year):
    date_obj = datetime.date(year, month, day)
    day_of_week = date_obj.strftime("%A")
    return day_of_week

def calculate_and_save(day, month):
    current_year = datetime.datetime.now().year

    file = open("birthday_days.txt", "w")
    file.write(f"Date: {day:02d}.{month:02d}\n")
    for i in range(current_year, current_year + 21):
      day_of_week = get_day_of_week(month, day, i)
      file.write(f"{day:02d}.{month:02d}.{i} - {day_of_week}\n")
    file.close()
    print("Результати збережено у файлі 'birthday_days.txt'.")


month = int(input("Введіть місяць вашого народження: "))
day = int(input("Введіть день вашого народження: "))
calculate_and_save(day, month)