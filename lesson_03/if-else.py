"""
if condition:
    operator1
    operator2
    operator3
operator4

if condition:
    operator1
    operator2
    operator3
else:
    operator4
    operator5
    operator6
operator7

if condition1:
    operator1
    operator2
    operator3
elif condition2:
    operator4
    operator5
    operator6
elif condition3:
    operator7
    operator8
    operator9
else:
    operator10
    operator11
    operator12

operator13
"""

a = 5

if a > 10:
    print('Variable more then 10')
else:
    print('Variable less then 10')
print('END')

b = -3
if b > 0:
    print('b > 0')
elif b < 0:
    print('b < 0')
else:
    print('b == 0')


s = 100
if 10 < s <= 100:          # 10 < s < 100
    print('1%')
elif 101 < s <= 1000:
    print('2%')
elif 1001 < s <= 10_000:
    print('5%')
elif 10_001 < s <= 100_000:
    print('10%')
elif 10_001 < s <= 100_000:
    print('10%')
elif 100_001 < s <= 1_000_000:
    print('15%')
else:
    print('more')


# 123  ==> 321 + 4 = 325
