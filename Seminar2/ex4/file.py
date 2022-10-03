# Кол-во вхождений одной строки в другую 

str1 = str(input('Введите первую строку: '))
str2 = str(input('Введите вторую строку: '))

count = 0
for i in str1:
    for j in str2:
        if i == j:
            print(i,j)
            count = count +1
print(f'Коли-во вхождений = {count}')