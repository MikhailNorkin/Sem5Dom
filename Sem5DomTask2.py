# 2- Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета(или сколько вы зададите). Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28 конфет(или сколько вы зададите). Тот, кто берет последнюю конфету - проиграл.
# Предусмотрите последний ход, ибо там конфет остается меньше.
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

import random

def user_move(candies):
    while True:
        try:
            num = int(input(f'На столе лежит {candies} конфет, укажите сколько вы возьмете конфет: '))
            return num
        except ValueError:
            print("Вы не ввели число!")

print()
print('Правила игры: 1. Выберете сколько на столе лежит конфет. 2. Выберете сколько за ход будет браться конфет. Проиграет тот, кто последний возьмет последнюю конфету')
random_number = random.randint(0, 1)
candies = int(input('Введите количество конфет: '))
number = int(input('Выберете сколько конфет будет браться за ход: '))
if random_number == 0:
    print('Бот будет ходить первым!')
else:
    print('Вы будете ходить первым!')   
move = random_number
while candies > 0:
    print()
    # ход бота
    if move == 0:
        print(f'На столе лежит {candies} конфет')
        # если конфет еще много, то бот берет все положенные за ход конфеты
        if candies > number+number+1:
            print(f'Бот берет {number} конфеты')
            candies = candies - number
        # если бот может сделать так, чтобы за ход осталась на столе одна конфета, то:
        elif candies > 1 :
            if candies == number+number:
                candies_bot = number-1
                print(f'Бот берет {candies_bot} ')
                candies = candies - candies_bot
            else:
                if candies > number:
                    candies_bot = number
                    print(f'Бот берет {candies_bot} ')
                    candies = candies - candies_bot
                else:
                    candies_bot = candies - 1
                    print(f'Бот берет {candies_bot} ')
                    candies = candies - candies_bot
        # если осталась одна конфета, то бот проиграл:
        if candies == 1:
            print('На столе осталась одна конфета! Вы выиграли!')
            candies = 0
        elif candies == 0:
            print('Бот выиграл!')
            candies = 0    
        move = 1
    else:
        # предложим ввести количество конфет, но необходимо учесть, что оставшееся количество конфет не должно быть меньше нуля:
        candies_user = user_move(candies)
        while candies - candies_user < 0:
            print('Вы не можете взять конфет больше, чем лежит на столе!')
            candies_user = user_move(candies)
        candies = candies - candies_user    
        if candies == 0:
            print('Бот выиграл!')
        move = 0    


            





