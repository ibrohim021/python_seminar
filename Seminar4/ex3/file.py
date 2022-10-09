pathRead = 'Seminar4/ex3/data.txt'
pathWrite = 'Seminar4/ex3/data2.txt'

try:
    with open(pathRead) as data:
        file = data.read().split(' ')
except:
    print('Файл ненайден!')

print(file)

# nam_int = int(file)
maxx = minn = int(file[0])

listNum = []
for i in range(len(file)):
    if file[i].isdigit():
        file[i] = int(file[i])
        listNum.append(file[i])

m = str((max(listNum)))
n = str((min(listNum)))
print(listNum)
print(max(listNum))
print(min(listNum))

try:
    with open(pathWrite, 'w') as data:
        file = data.write(f'max = {m}\n')
        file = data.write(f'min = {n}')
except:
    print('Файл ненайден!')
