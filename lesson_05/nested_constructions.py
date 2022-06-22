for _ in range(10):
    for _ in range(5):
        for _ in range(3):
            pass

rows = 11
cols = 11

for i in range(rows):
    for j in range(cols):
        if i == 0 or j == 0 or i == rows - 1 or j == cols - 1 \
                or i == j or rows - 1 - i == j \
                or i == rows // 2 or j == cols // 2:
            print('*  ', end='')
        else:
            print('   ', end='')
    print()
print()


for val2 in range(2, 10):
    print(2, 'x', val2, '=', 2*val2)
print()


for val1 in range(2, 10, 4):
    for val2 in range(2, 10):
        print('{v11:<2} x  {v12:<2} = {s1:<6}'
              '{v21:<2} x  {v22:<2} = {s2:<6}'
              '{v31:<2} x  {v32:<2} = {s3:<6}'
              '{v41:<2} x  {v42:<2} = {s4:<6}'.format(
                v11=val1, v12=val2, s1=val1 * val2,
                v21=val1+1, v22=val2, s2=(val1+1) * val2,
                v31=val1+2, v32=val2, s3=(val1+2) * val2,
                v41=val1+3, v42=val2, s4=(val1+3) * val2)
        )
    print()
    print()
print()


for val1 in range(1, 10):
    for val2 in range(1, 10):
        if val1 == 1 and val2 == 1:
            print('', end='    ')
            continue
        if val1 == 1:
            print(val2, end='   ')
            continue

        print('{:<4}'.format(val1*val2), end='')
    print()
print()
print()
