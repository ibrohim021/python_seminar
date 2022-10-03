import random

num = int(input('Введите число: '))

arr = []

for i in range(num):
    arr.append(random.randint(-num, num))
print(arr)

position = ''

with open('text.txt', 'r') as data:
    position = data.read().split('\n')

print(arr[int(position[0]) * int(position[1])])