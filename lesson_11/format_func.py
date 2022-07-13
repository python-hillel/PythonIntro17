# str.format()

# Len of the number: 235324324                          is 9
# Len of the number: 234324                             is 6
# Len of the number: 23532434534534324                  is 17
# Len of the number: 2353234534234234234233424234324    is 31

temp = 'Len of the number: {:>32} is {:<4}'
a = [34532534, 45754645, 568544523, 8566435423, 25375436436356345324535636653, 678657, .23423]
for number in a:
    print(temp.format(number, len(str(number))))

#  { field_name !modifier : specification }

# !r, !s, !a
# __str__, __repr__, __ascii__

#  fill align sign width .precision type
# align: > < = ^
# +0000034
# 0000+34
# +34

# sign: + -
# +     34

# 10.2

# type:
# b - binary
# c - symbol
# d, i, u, n - integer
# o - oct
# x, X - hex
# e, E
# s - string
# f, F - float

coord = (3, 5)
number = 343
string = 'Hello'
print('X: {0[0]};  Y: {0[1]}; Number: {1}; String: {2}'.format(coord, number, string))

print("repr() shows quotes: {!r}; str() doesn't: {!s}".format('test1', 'test2'))

print('"{:<30}"'.format('left aligned'))                 # 'left aligned                  '
print('"{:>30}"'.format('right aligned'))                # '                 right aligned'
print('"{:^30}"'.format('centered'))                     # '           centered           '
print('"{:*^30}"'.format(' centered '))                  # '********** centered **********'

# 03:05:09

print('"{:+f}"; "{:+f}"'.format(3.14, -3.14))              # '+3.140000; -3.140000'
print('"{: f}"; "{: f}"'.format(3.14, -3.14))              # ' 3.140000; -3.140000'
print('"{:-f}"; "{:-f}"'.format(3.14, -3.14))              # '3.140000; -3.140000'
print('"{:-5.1f}"; "{:-7.2f}"'.format(3.16, -3.14))              # '3.140000; -3.140000'

print("int: {0:d};  hex: {0:x};  oct: {0:o};  bin: {0:b}".format(37))
print('int: {0:d};  hex: {0:#x};  oct: {0:#o};  bin: {0:#b}'.format(37))

points = 19.5
total = 22
print('Correct answers: {:.2%}'.format(points/total))     # 'Correct answers: 88.64%'
v1 = 23
v2 = 34
print('Value 1: {val1:>5}\nValue 2: {val2:>5}\n{val1:>5} + {val2:>5} = {res:>5}'.format(
    val1=v1, val2=v2, res=v1+v2
))

val1 = 45
val2 = 67
print(f'Value 1: {val1:>5}\nValue 2: {val2:>5}\n{val1:>5} + {val2:>5} = {val1+val2:>5}')
