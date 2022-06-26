from random import randint

lst = []
for _ in range(30):
    lst.append(randint(10, 99))
print(lst)

lst1 = [randint(10, 99) for _ in range(30)]
print(lst1)

lst2 = [value for value in lst1 if value % 2 == 0]
print(lst2)

# variable = [expression1 expression2 expression3]
# variable = [expression1 expression2]

# 96 + 34 + 75 + .... + 42 + 95 = sum
# sum()
# join()

res = ' + '.join([str(element) for element in lst]) + ' = ' + str(sum(lst))
print(res)
