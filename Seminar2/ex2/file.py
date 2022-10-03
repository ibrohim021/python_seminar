from unittest import result


Number = int(input('введите чсло: '))

result = []
for deggre in range(Number+1):
    result.append((-3)**deggre)

print(result)