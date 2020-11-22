import random
num = random.randint(1, 100)
# Введение
print("ДОБРО ПОЖАЛОВАТЬ В ИГРУ УГАДАЙ ЧИСЛО!")
print("Я загадал число от 1 до 100")
print("Если Ваша отгадка дальше чем на 10 от моего числа, то я скажу вам ХОЛОДНО")
print("Если Ваша отгадка ближе чем на 10 от моего числа, то я скажу вам ТЕПЛО")
print("Если Ваша отгадка дальше чем предыдущая отгадка, то я скажу вам ХОЛОДНЕЕ")
print("Если Ваша отгадка ближе чем предыдущая отгадка, то я скажу вам ТЕПЛЕЕ")
print("НАЧНЁМ ИГРУ!")
# Список для хранения отгадок
guesses = [0]

while True:

    guess = int(input("Я загадал число от 1 до 100.\n  Какая Ваша отгадка? "))

    if guess < 1 or guess > 100:
        print('ВНЕ ДИАПАЗОНА! Попробуйте еще: ')
        continue
    # здесь мы сравниваем отгадку игрока с загаданным числом
    if guess == num:
        print(f'ПОЗДРАВЛЯЮ, ВЫ УГАДАЛИ, ЭТО ЗАНЯЛО {len(guesses)} ПОПЫТОК!!')
        break
    # если отгадка неправильна, то добавляем ее в список
    guesses.append(guess)
    # при проверке первой отгадки, guesses[-2]==0, то есть это условие False
    # и мы переходим к разделу else
    if guesses[-2]:
        if abs(num-guess) < (num-guesses[-2]):
            print('ТЕПЛЕЕ!')
        else:
            print('ХОЛОДНЕЕ!')
    else:
        if abs(num-guess) <= 10:
            print('ТЕПЛО!')
        else:
            print('ХОЛОДНО!')


