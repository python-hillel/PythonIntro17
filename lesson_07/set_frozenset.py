from random import randint

s = {}
print(type(s), s)
s = set()
print(type(s), s)
string = 'Hello World!'
lst = [1, 2, 3, 4, 2, 5, 6, 3, 5, 1]
t = (7, 5, 8, 4, 9, 0, 1, 0)
# {1, 3, 6, 2}
print(set(string))
print(set(lst))
print(set(t))

s = set(string)
for el in s:
    print(el, end=' ')
print()

s.add(5)
print(s)
s.add('r')
print(s)
s.remove('r')
print(s)
s.discard(55)
print(s)
a = s.pop()
print(a, s)

s1 = {35, 39, 41, 10, 43, 12, 13, 44, 17, 18, 21, 23, 25, 27, 29, 30, 31}   # set([randint(10, 50) for _ in range(20)])
s2 = {32, 33, 34, 35, 37, 40, 41, 42, 45, 14, 48, 17, 50, 20, 27}           # set([randint(10, 50) for _ in range(20)])
print(s1)
print(s2)

"""
C = A | B                       C = A.union(B)
A |= B                          A.update(B)
"""
s3 = s1 | s2
print(s3)

"""
C = A & B                       C = A.intersection(B)
A &= B                          A.intersection_update(B)
"""
s3 = s1 & s2
print(s3)

"""
C = A - B                       C = A.difference(B)
A -= B                          A.difference_update(B)
"""
s3 = s1 - s2
print(s3)

"""
C = A ^ B                       C = A.symmetric_difference(B)
A ^= B                          A.symmetric_difference_update(B)
"""
s3 = s1 ^ s2
print(s3)

s4 = s1 - s2
s5 = s2 - s1
s6 = s4 | s5
print(s6)

print(frozenset(string))
print(frozenset(lst))
print(frozenset(t))
print(frozenset(s1))
