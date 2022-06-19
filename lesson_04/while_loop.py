"""
while condition:
    operator1
    operator2
operatorN
"""

i = 0
while i < 25:
    i += 1
    print(i, end=' -> ')
print()

a = 1
a = b = c = d = 0
a, b, c, d = 0, 1, 2, 3
print(a, b, c, d, sep='\n')     # a sep b sep c sep d end

# n = int(input('Введите целое, положительное число: '))
# # 4388 // 10 = 438
# # 438 // 10 = 43
# # 43 // 10 = 4
# # 4 // 10 = 0
# cnt = 0
# while n != 0:
#     cnt += 1
#     n //= 10
# print('Количество цифр: ', cnt)
#
#
# # break
# n = int(input('Введите целое, положительное число: '))
# cnt = 0
# while True:
#     if n == 0:
#         break
#     cnt += 1
#     n //= 10
#
# print('Количество цифр: ', cnt)
i = 1
while i <= 100:
    if not i % 2:
        print(i, end=' ')
    i += 1
print()


i = 0
while i <= 100:
    i += 1
    # if i % 2 != 0:
    if i % 2:
        continue
    print(i, end=' ')
print()


i = 1
while i < 100:
    if i > 23:
        break
    print(i, end=' ')
    i += 1
else:
    print('ELSE in WHILE')
