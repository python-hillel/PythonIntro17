from copy import deepcopy

t = ()
print(type(t), t)
t = tuple()
print(type(t), t)
lst = [1, 2, 3, 4, 5]
s = 'Hello World!'
t = tuple(lst)
print(type(t), t)
t = tuple(s)
print(type(t), t)
t = (1, 2, 'test', True, 4.5)
print(type(t), t)

var = 50, True, 'Test'
print(var, type(var))
t = (50, True, 'Test')
a, b, c = t
a, b, c = 50, True, 'Test'
print(a, b, c)

w = 5
e = w
print(e, id(e))
print(w, id(w))

lst1 = [1, 2, 3, 4, 5]
lst2 = lst1
print(lst1, id(lst1))
print(lst2, id(lst2))
lst1[2] = 88
print(lst1, id(lst1))
print(lst2, id(lst2))

lst3 = []
for el in lst1:
    lst3.append(el)

print(lst3, id(lst3))
lst1[3] = 99
print(lst1, id(lst1))
print(lst3, id(lst3))

lst4 = lst1.copy()
print(lst4, id(lst4))

lst5 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(len(lst5))
print(lst5[0][1])
lst6 = lst5.copy()
print(lst5, id(lst5))
print(lst6, id(lst6))
lst5[1][1] = 88
print(lst5, id(lst5))
print(lst6, id(lst6))

# for i in range(len(lst5)):
#     for j in range(len(lst5[i])):
#         print(f'{id(lst5[i][j])} - {id(lst6[i][j])} - [{i}][{j}]')
for i in range(len(lst5)):
    print(f'{id(lst5[i])} - {id(lst6[i])} - [{i}]')

lst7 = deepcopy(lst5)
print(lst5, id(lst5))
print(lst7, id(lst7))
lst5[1][1] = 33
print(lst5, id(lst5))
print(lst7, id(lst7))
for i in range(len(lst5)):
    print(f'{id(lst5[i])} - {id(lst7[i])} - [{i}]')


