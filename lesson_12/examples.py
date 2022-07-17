lst = [
    [10, 24, 37, 20],
    [44, 52, 67, 83],
    [72, 87, 93, 16]
]

res = list(map(lambda a: (a[0], a[2]), lst))
print(res)

for i in range(len(lst)):
    for j in range(len(lst[i])):
        # print('{:>3}'.format(lst[i][j]), end='')
        print(f'{lst[i][j]:>3}', end='')
    print('\t43654')
print()


def func(value):
    print(value)
