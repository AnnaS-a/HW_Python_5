# Задача2: Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

# ОТВЕТ: Первому  игроку  надо первым ходом забрать остаток от целочисленного деления
# имеющегося количества конфет на то, которое можно взять за 1 ход максимально + 1
# В дальнейшем первому игроку нужно повторять стратегию.
# Пример :  2021 % ( 28 + 1 ) = 20 , первый игрок первым ходом должен взять 20 конфет.
# если вторым ходом второй игрок взял 10 конфет, то первый должен взять 28 + 1 - 10 = 19 и так далее..
import random    
   
user_number = None    
user_count = int(1)   
users = []    
for i in range(user_count):
    u = 'bot'
    users.append(u)
    user_name = input(f'Введите имя пользователя: ') 
    users.append(user_name)
print(users)

is_winner = False   
winner_name = None  
k = 61 
step_max = 28
step_1 = [k / step_max + 1]
count = 1
candies = int(k)
while not is_winner:  #  пока у нас нет победителя крутит цикл
    for user in users:       # пока этот пользовательесть в списке
        if candies > 0:
            print(f'Ход пользователя {user}')
            if user == 'bot':
                if count == 1:
                    user_number = k % (step_max + 1)
                    print(f'бот забирает конфет: {user_number}')
                    candies = candies - user_number
                    print(candies)
                else: 
                    user_number = step_max + 1 - user_number 
                    print(f'бот забирает конфет: {user_number}') 
                    candies = candies - user_number 
                    print(candies)  
            else:    
                user_number = int(input('Введите количество конфет (не более 28): ')) 
                if user_number > step_max:
                    print('Ввели число больше 28.')
                    break 
                else:
                    candies = candies - user_number   
                    print(candies)              
            count += 1    
            if candies <= 0:      
                is_winner = True      
                winner_name = user          
else:
    print(f'Победитель {winner_name}')
