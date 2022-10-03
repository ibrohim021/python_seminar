# Программа находит точное совпадение слов и показывает индекс 2го вхождения


list_elem = ['man', 'dog', 'pap', 'mas', 'man']
word = 'man'

for  i in range(len(list_elem)):
    if list_elem[i] == word:
        print('индекс 2 го вхождения = ',i)
        
        
        