# поиск элементов по индексу

arr = ['man','cat','home','dog']

serch = int(input('Введите число для поиска: '))

for i in range(len(arr)):
    if serch == i:
        print('Результат поиска = ', arr[i])
