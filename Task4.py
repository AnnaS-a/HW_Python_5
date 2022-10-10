# Задача4: Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

def read_elements(file):
    with open(str(file), 'r') as f:
        elem = f.read() 
    return elem

file = 'C:\\Users\\Sluki\\Desktop\\ГБ Лекции Семинары\\Работы Python\\HW_Python_5\\task4_1.txt'
res = read_elements(file)
print(res)

rle_code = []
r = None
for d in res:
    if d != r:
        rle_code.append(d)
        rle_code.append(str(1))
        r = d
    else:
        rle_code[-1] = str(int(rle_code[-1]) + 1)
print("".join(rle_code))

def write_file(st):
    with open('task4_1_1.txt', 'w') as data:
        data.write(st)

write_file("".join(rle_code))



def read_elements(file):
    with open(str(file), 'r') as f:
        elem = f.read() 
    return elem

file = 'C:\\Users\\Sluki\\Desktop\\ГБ Лекции Семинары\\Работы Python\\HW_Python_5\\task4_2.txt'
res = read_elements(file)
print(res)


def rle_decode(txt):
    elem = ''
    res = ''
    for i in range(len(txt)):
        if not txt[i].isalpha():
            elem += txt[i]
        else:
            res = res + txt[i] * int(elem)
            elem = ''
    return res

result = rle_decode(res)
print(result)

def write_file(st):
    with open('task4_2_1.txt', 'w') as data:
        data.write(st)

write_file(result)

