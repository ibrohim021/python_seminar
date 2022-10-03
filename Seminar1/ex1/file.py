# создаем массив из 5 элементов

array = []
for i in range(5):
    array.append(int(input(f'Введите число {i+1}: ')))
print()

print('Создали масив:')
print()

for i in array:
    print(i, end =" ")
print()
print()

print('Показали индексы элементов:')

print()
for j in range(len(array)):
    
    print(f'Индекс элемента {array[j]} = {[j]} ' ,  end =" ") 
