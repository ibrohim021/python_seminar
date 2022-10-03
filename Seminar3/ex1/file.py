
# Найдем сумму числа: 23 = 5, 44 = 8




number = input('Введите число: ')

summa = 0

for i in number:
    if i.isdigit():
        summa += int(i)

print(f'Сумма числа = {summa}')