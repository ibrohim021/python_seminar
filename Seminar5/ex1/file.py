dict = {1:'man', 2:'cat', 3:'star', 4:'dog'}

if dict.get(4):
    print('Есть элемент')

for i in dict.items():
    print(*i)
