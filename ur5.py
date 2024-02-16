# monthDict = {'January': 31, 'February': 28, 'March': 31, 'April': 30, 'May': 31}
#
# month_input = input("Введіть назву місяця: ")
#
# if month_input in monthDict:
#     days_in_month = monthDict[month_input]
#     print(f'{month_input} має {days_in_month} днів')
# else:
#     print('Введено некоректний місяць')


import os
project_path = 'main.py'
# idea_path = os.path.join(project_path, '.idea')
if os.path.exists(project_path):
    print(f'Шлях до папки .idea в проекті {project_path} існує.')
else:
    print(f'Шлях до папки .idea в проекті {project_path} не існує.')
