import random

def validate_input(choice):
    try:
        choice = int(choice)
        if choice < 1 or choice > 3:
            raise ValueError
        return choice
    except ValueError:
        print("Введено не число или неправильное колличество камней")


def computer_turn(stones):
    computer_choice = random.randint(1, min(3, stones))
    if computer_choice == 1:
        print("Компьютер берет", computer_choice, "камень.")
    else:
        print("Компьютер берет", computer_choice, "камня.")
    return stones - computer_choice


def user_turn(stones):
    valid_choice = False
    while not valid_choice:
        user_choice = input("Твой ход. Сколько камней ты хочешь взять (1, 2, или 3)? ")
        user_choice = validate_input(user_choice)
        if user_choice <= stones:
            return stones - user_choice


def play_game():
    stones = random.randint(4, 30)
    print("Колличество камней в куче:", stones)
    while stones > 1:
        stones = user_turn(stones)
        print("Колличество оставшихся камней:", stones)
        if stones == 1:
            print("Ты победил!")
            return 0
        if stones == 0:
            print("Компьютер выйграл")
            return 0
        stones = computer_turn(stones)
        print("Колличество оставшихся камней:", stones)
        if stones == 1:
            print("Компьютер выйграл!")
            return 0


play_game()