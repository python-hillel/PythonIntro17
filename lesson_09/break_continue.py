# continue
# 873456 % 348795643078564387652478634879654786534897654387965298 = 873456

# for i in range(10):
#     if i % 2:
#         continue
#     print(i, end=' ')
# print()

# break
# for i in range(25):
#     if i > 15:
#         break
#     print(i, end=' ')
# print()

number_sum = 0
number_cnt = 0
min_number = 0
max_number = 0
even_cnt_numbers = 0
odd_cnt_number = 0

while True:
    n = int(input('Введите число: '))
    if n == 0:
        break

    number_sum += n
    number_cnt += 1

    # if number_cnt == 1:
    #     max_number = n
    #     min_number = n

    if max_number == 0 or n > max_number:
        max_number = n

    if min_number == 0 or n < min_number:
        min_number = n

    if n % 2:
        odd_cnt_number += 1
    else:
        even_cnt_numbers += 1

print('Even:', even_cnt_numbers)
print('Odd:', odd_cnt_number)
print('Sum:', number_sum)
print('Cnt:', number_cnt)
print('Min:', min_number)
print('Max:', max_number)
print('Avr:', round(number_sum / number_cnt, 2))

print('----------------------------------------------')

n = int(input('Введите число: '))
number_sum = 0
number_cnt = 0
min_number = n
max_number = n
even_cnt_numbers = 0        # int(not n % 2)   # 0 if n % 2 else 1
odd_cnt_number = 0          # int(n % 2)       # 1 if n % 1 else 0

while n != 0:
    number_sum += n
    number_cnt += 1

    if n > max_number:
        max_number = n

    if n < min_number:
        min_number = n

    if n % 2:
        odd_cnt_number += 1
    else:
        even_cnt_numbers += 1

    n = int(input('Введите число: '))

print('Even:', even_cnt_numbers)
print('Odd:', odd_cnt_number)
print('Sum:', number_sum)
print('Cnt:', number_cnt)
print('Min:', min_number)
print('Max:', max_number)
print('Avr:', round(number_sum / number_cnt, 2))


"""
++A
--B

if (a < b || a++)

"""
