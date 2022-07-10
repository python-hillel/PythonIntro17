import datetime
from random import randint

"""
lambda arg1, arg2: arg1 + 45 / arg2
"""

func = lambda arg1, arg2: arg1 + 45 / arg2
res = func(34, 65)
print(res)

print((lambda arg1, arg2: arg1 + 45 / arg2)(2, 6))

# map
# filter

# zip

# MAP
# map(func, iterable_obj)


def fahrenheit(temperature):
    return round(((float(9)/5)*temperature + 32), 2)


def celsius(temperature):
    return round((float(5)/9)*(temperature-32), 2)


temperatures = (36.5, 37, 37.5, 38, 39)

lst_F = []
for t in temperatures:
    lst_F.append(fahrenheit(t))
print(lst_F)

lst_C = []
for t in lst_F:
    lst_C.append(celsius(t))
print(lst_C)


F = map(fahrenheit, temperatures)
l_F = list(F)
print(l_F)
C = map(celsius, l_F)
# for c in F:
#     print(c)
print(list(C))

ll_F = list(map(lambda t: round(((float(9) / 5) * t + 32), 2), temperatures))
print(ll_F)
ll_C = list(map(lambda t: round((float(5) / 9) * (t - 32), 2), ll_F))
print(ll_C)


# FILTER
# filter(func, iterable_obj)
lst = [randint(10, 99) for _ in range(30)]
print(lst)

lst_E = []
for e in lst:
    if e % 2 == 0:
        lst_E.append(e)
print(lst_E)

lst_EE = list(filter(lambda x: x % 2 == 0, lst))
print(lst_EE)

lst_OO = list(filter(lambda x: x % 2, lst))
print(lst_OO)

# ZIP

# zip(iter1, iter2, ... iterN)
l1 = [randint(10, 9999) for _ in range(10 ** 6)]     # [70, 58, 82, 12, 36, 88, 50, 54, 92, 38, 26, 46, 42, 74]
l2 = [randint(10, 9999) for _ in range(10 ** 7)]     # [49, 75, 77, 45, 13, 79, 49, 25, 91, 67, 55, 45, 95, 41, 55, 85]
# l3 = zip(l1, l2)
# print(dict(l3))
l4 = [randint(10, 9999) for _ in range(10 ** 7)]     # [99, 29, 37, 49, 93, 41, 79, 41, 95, 57, 83, 63, 33, 75, 35, 41]
l5 = [randint(10, 9999) for _ in range(10 ** 7)]     # [60, 22, 96, 32, 22, 20, 86, 36, 24, 34, 40, 30, 50]

start = datetime.datetime.now()
l6 = list(zip(l1, l2, l4, l5))
print(datetime.datetime.now() - start)
# print(l6)

l0 = []
start = datetime.datetime.now()
for i in range(min(len(l1), len(l2), len(l4), len(l5))):
    l0.append((l1[i], l2[i], l4[i], l5[i]))
print(datetime.datetime.now() - start)
# print(l0)



