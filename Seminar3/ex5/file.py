spisok  = ['home', 'man', 'cat', 'dog']

serch_file = input('Введите слово: ')

for elem in spisok:
    if serch_file == elem:
        print('Это слово есть в массиве')
        break
else:
    print('такого слова нет')
    