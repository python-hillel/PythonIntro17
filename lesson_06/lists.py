lst = []
print(type(lst), lst)
lst = list()
print(type(lst), lst)
lst = list('Hello World!')
print(type(lst), lst)
lst = [4, 6, 2.3, True, 'string', print]
# lst[5]('Hello World!')

# index, slice, len
lst1 = [1, 2, 3]
lst2 = [4, 5, 6]
lst3 = lst1 + lst2
print(lst3)
lst4 = lst1 * 3
print(lst4)
lst5 = [0] * 10
print(lst5)

s = 'Hello World!'              # 0 - (N-1)
lst6 = [4, 6, 2.3, 'string']

for i in range(len(s)):         # 0 - (N-1) - 1
    print(s[i], end=' ')
print()

for i in range(len(lst6)):         # 0 - (N-1) - 1
    print(lst6[i], end=' ')
    lst6[i] *= 3
print()

lst6[1] = 88888
print(lst6)

for element in s:
    print(element, end=' ')
print()

for element in lst6:         # 0 - (N-1) - 1
    print(element, end=' ')
print()

lst = [1, 2, 3, 4, 5, 6]
# len(list)
print(len(lst))

# list.append(value)
print(lst, id(lst))
lst.append(99)
print(lst, id(lst))

# min(list), max(list), sum(list)
print(min(lst))
print(max(lst))
print(sum(lst))

# in, not in
print(7 in lst)
print(5 not in lst)

# list.index(value)
print(lst.index(6))

# list.count(value)
lst *= 3
print(lst)
print(lst.count(1))

# list.pop()
x = lst.pop()
print(lst)
print(x)
x = lst.pop()
print(lst)
print(x)

# list.pop(idx)
x = lst.pop(6)
print(x)
print(lst)

# list.insert(idx, value)
# 1 2 3 4 5  --> 88, 2  ---> 1 2   3 4 5 ----> 1 2 88 3 4 5
lst.insert(6, 88)
print(lst)

# list.clear()
# lst.clear()
# print(lst)

# list.extend(list1)
l1 = [1, 2, 3]
l2 = [4, 5, 6]
l3 = l1 + l2
print(id(l1), id(l2), id(l3))
print(l1, l2, l3)
l1.extend(l2)
print(l1, l2)
print(id(l1), id(l2))

# list.remove(value)
lst.remove(88)
print(lst)

# del list[idx]
del lst[2]
print(lst)

# del lst
# print(lst)

# list.reverse()
# list[::-1]
print(lst, id(lst))
lst.reverse()
print(lst, id(lst))
lst2 = lst[::-1]
print(lst2, id(lst2))
print(lst, id(lst))

# split, join
s = 'Process finished with exit code 0'
lst = s.split()
print(lst)
ss = ' + '.join(lst)
print(ss)



