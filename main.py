import random

print("Вітаю в грі 'Вгадай число'!")
player_name = input("Введи свій нікнейм: ")
print("Привіт, {player_name}! Почнемо гру!")

attempts_history = []

while True:
    secret_number = random.randint(1, 50)
    attempts = 0

    print("Я загадав число від 1: до 50:. Спробуй вгадати!")

    while True:
        user_input = input("Введи,свій варіант: ")


        if user_input.isdigit():
            guess = int(user_input)
            attempts += 1

            if guess < secret_number:
                print("Моє число більше!")
            elif guess > secret_number:
                print("Моє число менше!")
            else:
                print("Вітаю, {player_name}! Ти вгадав число {secret_number}!")
                print("Кількість спроб: {attempts}")
                attempts_history.append(attempts)
                break
        else:
            print("Помилка! Потрібно вводити тільки цілі числа.")
    play_again = input("Хочеш зіграти ще раз? (так/ні): ").lower()
    if play_again != "так":
        break
print("Історія твоїх раундів (кількість спроб у кожному):")
print(attempts_history)
print("Дякую за гру)!")
