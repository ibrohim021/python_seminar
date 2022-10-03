n = int(input('число '))

# array_num = [1,3,4,6,8,9,10]
print()

print('Выели числа от -n до n:')

print()

for i in range(-n, n+1):
    print(i, end=" ")

print()
print()

print('Сортировка по четным числам:') 

print()

for i in range(-n, n+1):
    if i%2 == 0:
        print(i, end=" ")