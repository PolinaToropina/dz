import random

def truth_or_dare():
    truth_questions = [
        "Чи є у тебе таємниця?",
        "У тебе день народження влітку?",
        "Ти любиш солодке?",
    ]

    dare_actions = [
        "Зроби уроки.",
        "Прочитай одну сторінку книги.",
        "Пострибай 10 разів.",
    ]

    while True:
        print("Правда або дія?")
        choice = input("Введіть 'п' для правди або 'д' для дії: ").lower()

        if choice == 'п':
            truth_question = random.choice(truth_questions)
            answer = input(truth_question + " ")
            print(f"Твоя відповідь: {answer}")
        elif choice == 'д':
            dare_action = random.choice(dare_actions)
            print(f"Виконай дію: {dare_action}")
        else:
            print("Будь ласка, введіть 'п' або 'д'.")

        repeat = input("Хочете грати ще раз? (так/ні): ").lower()
        if repeat != 'так':
            break

if __name__ == "__main__":
    truth_or_dare()


