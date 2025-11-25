import random

print("Вітаю у грі 'Вгадай число'!")

while True:
    nickname = input("Введи свій нікнейм: ")
    print(f"Привіт, {nickname}! Я загадав число від 1 до 50. Спробуй вгадати!")

    secret_number = random.randint(1, 50)
    attempts = 0

    while True:  # Цикл однієї гри
        user_input = input("Введи свій варіант: ")


        if user_input.isdigit():
            guess = int(user_input)
            attempts += 1
