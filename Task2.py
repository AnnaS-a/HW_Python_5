# Задача2: Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

user_number = None    
user_count = int(2)   
users = []    
for i in range(user_count):
    user_name = input(f'Введите имя пользователя {i+1}: ') 
    users.append(user_name)
print(users)

k = 2021 
step_max = 28
is_winner = False   
winner_name = None   
candies = int(k)
while not is_winner:  
    for user in users:       
        if candies > 0:
            print(f'Ход пользователя {user}')
            user_number = int(input('Введите количество конфет (не более 28): ')) 
            if user_number > step_max:
                print('Ввели число больше 28.')
                break
            candies = candies - user_number      
            if candies <= 0:      
                is_winner = True      
                winner_name = user   
else:
    print(f'Победитель {winner_name}')
