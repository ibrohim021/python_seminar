# Создать словари примера: Индекс = Значение
# Пример: 1 = мир, 2 = 45, 3 = свет

Input_user = int(input('Введите число '))

match Input_user:
    case 1:
        print('Мир')
    case 2:
        print('Свет')
    case 3:
        print('Дом')
    case 4:
        print('Семья')