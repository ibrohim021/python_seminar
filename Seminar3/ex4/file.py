
array_list = ['45', 'home', 'cat', 'dog35']

a = False

for i in range(len(array_list)):
    if array_list[i].isdigit():
        print('В списке есть число')
        a = True
        break
if a == False:
    print('Числа нет')


