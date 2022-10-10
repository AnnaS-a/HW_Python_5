# Задача1: Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

input_text = input('Введите текст: ')
text1 = "абв"
text_list = input_text.split()
result = []
for word in text_list:
    if text1 not in word:
        result.append(word)
print("".join(result))
