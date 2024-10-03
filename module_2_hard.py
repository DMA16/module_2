import os


clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')


def user_input_number():
    is_the_previous_input_incorrect = False
    while True:
        clear()

        if is_the_previous_input_incorrect:
            print("Некорректный ввод!")

        n = input("Введите число от 3 до 20: ")

        if not n.isnumeric():
            is_the_previous_input_incorrect = True
            continue

        n = int(n)
        if not (3 <= n <= 20):
            is_the_previous_input_incorrect = True
            continue

        return n

def find_multiples(num):
    multiples = []
    for i in range(3, num + 1):
        if num % i == 0:
            multiples.append(i)

    return multiples

def get_password(user_number, numbers):
    password = ''
    for i in range(1, user_number):
        for number in numbers:
            second_number = number - i

            if second_number > 0 and second_number > i:
                password = password + str(i) + str(second_number)

    return password

def start():
    user_number = user_input_number()

    multiples = find_multiples(user_number)

    password = get_password(user_number, multiples)

    print("Пароль:", password)
    
start()
