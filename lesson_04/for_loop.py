# range(start, stop, step)
# range(start, stop)        step = 1
# range(stop)               start = 0, step = 1
"""
    range(1, 20, 3)     1, 4, 7, 10, 13, 16, 19
    range(1, 10)        1, 2, 3, 4, 5, 6, 7, 8, 9
    range(10)           0, 1, 2, 3, 4, 5, 6, 7, 8, 9

for variable in iter_obj:
    operator1
    operator2
operatorN

for _ in iter_obj:
    operator1
    operator2
operatorN
"""

s = "Hello World!"
for var in s:
    print(var, end='')
print()

for var in range(10):
    print(var, end=' ')
print()

for var in range(1, 10):
    print(var, end=' ')
print()

for var in range(2, 25, 2):
    print(var, end=' ')
print()

for _ in range(5):
    print('Hello World!')

for v in range(50):
    if v % 2:
        continue
    print(v, end=' ')
print()

for v in range(50):
    if v >= 25:
        break
    print(v, end=' ')
print()

# x, y
number_1 = int(input('Введите начало диапазона: '))
number_2 = int(input('Введите конец диапазона: '))
summa = 0
for num in range(number_1, number_2+1):
    summa += num
print('Сумма чисел: ', summa)
