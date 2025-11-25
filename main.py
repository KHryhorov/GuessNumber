import random


while True:
    secret_number = random.randint(1, 50)
    attempts = 0

        user_input = input("Введи свій варіант: ")


        if user_input.isdigit():
            guess = int(user_input)
            attempts += 1
