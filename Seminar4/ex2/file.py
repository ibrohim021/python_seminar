import random

arr =[]

def fillArray(list):
    list.clear()
    for i in range(10):
        list.append(random.randint(-5, 5))
    return list

print(arr)
fillArray(arr)
print(arr)