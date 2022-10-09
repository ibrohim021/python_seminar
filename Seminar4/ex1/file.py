from curses.ascii import isdigit


number = '-43.342werew234'

summa =0
for i in number:
    if i.isdigit():
        summa += int(i)
print(summa)

