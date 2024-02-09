import random

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "Нічия"
    elif (
        (player_choice == "камінь" and computer_choice == "ножиці") or
        (player_choice == "ножиці" and computer_choice == "папір") or
        (player_choice == "папір" and computer_choice == "камінь") or
        (player_choice == "камінь" and computer_choice == "ящірка") or
        (player_choice == "ящірка" and computer_choice == "спок") or
        (player_choice == "спок" and computer_choice == "ножиці") or
        (player_choice == "ножиці" and computer_choice == "ящірка") or
        (player_choice == "ящірка" and computer_choice == "папір") or
        (player_choice == "папір" and computer_choice == "спок") or
        (player_choice == "спок" and computer_choice == "камінь")
    ):
        return "Гравець перемагає!"
    else:
        return "Комп'ютер перемагає!"

def play_game():
    choices = ["камінь", "ножиці", "папір", "ящірка", "спок"]
    player_score = 0
    computer_score = 0

    while True:
        player_choice = input("Введіть свій вибір (камінь, ножиці, папір, ящірка або спок): ").lower()

        if player_choice not in choices:
            print("Будь ласка, введіть правильний вибір.")
            continue

        computer_choice = random.choice(choices)
        print(f"Комп'ютер обрав: {computer_choice}")

        result = determine_winner(player_choice, computer_choice)
        print(result)

        if "Гравець" in result:
            player_score += 1
        elif "Комп'ютер" in result:
            computer_score += 1

        print(f"Стан гри: Гравець {player_score}, Комп'ютер {computer_score}")

        if player_score == 3:
            print("Гравець переміг у серії! Вітаємо!")
            break
        elif computer_score == 3:
            print("Комп'ютер переміг у серії. Спробуйте ще раз.")
            break

if __name__ == "__main__":
    while True:
        play_game()
        play_again = input("Бажаєте зіграти ще раз? (так/ні): ").lower()
        if play_again != "так":
            break

