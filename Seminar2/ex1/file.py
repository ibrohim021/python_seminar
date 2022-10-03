a = 4
b = a  
a += 5 
print(b)

# Чему равно b ?

print()

a = [1,2,3]
b = a
a.append(4)
print(f'мвссив a = {a}')
print()

print(f'массив b = {b}')

print()

c = a.copy()
c.append(6)
c.append(12)
print(f'массив c =  {c}')


a = int(input('Введите день недели - цифру: '))
match a:
    case 1:
        print('Понедельник')
    case 2:
        print('Вторник')
    case 3:
        print('Среда')
    case 4:
        print('Четверг')
    case 5:
        print('Пятница')
    case 6:
        print('Суббота')
    case 7:
        print('Воскресенье')
    case _ :
        print('Чет не то ! В неделе только 7 дней')
