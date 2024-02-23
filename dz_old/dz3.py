import random

item={}
item["stone"]="камінь"
item["scissors"]="ножиці"
item["paper"]="папір"
item["lizard"]="ящірка"
item["spok"]="спок"


def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "Нічия"
    elif (
        (player_choice == item["stone"] and computer_choice == item["scissors"]) or
        (player_choice == item["scissors"] and computer_choice == item["paper"]) or
        (player_choice == item["paper"] and computer_choice == item["stone"]) or
        (player_choice == item["stone"] and computer_choice == item["lizard"]) or
        (player_choice == item["lizard"] and computer_choice == item["spok"]) or
        (player_choice == item["spok"] and computer_choice == item["scissors"]) or
        (player_choice == item["scissors"] and computer_choice == item["lizard"]) or
        (player_choice == item["lizard"] and computer_choice == item["paper"]) or
        (player_choice == item["paper"] and computer_choice == item["spok"]) or
        (player_choice == item["spok"] and computer_choice == item["stone"])
    ):
        return "Гравець перемагає!"
    else:
        return "Комп'ютер перемагає!"

def play_game():
    choices = [item["stone"], item["scissors"], item["paper"], item["lizard"], item["spok"]]
    player_score = 0
    computer_score = 0

    while True:
        player_choice = input(f"Введіть свій вибір ({item['stone']}, {item['scissors']}, {item['paper']}, {item['lizard']} або {item['spok']}): ").lower()

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



