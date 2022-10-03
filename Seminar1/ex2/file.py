# Найти максимальное число в массиве

array = []
for i in range(5):
    array.append(int(input(f'Введите число {i+1}: ')))

max = array[0]
for i in array:
    if max < i:
        max = i
print(f'Max = {max}')