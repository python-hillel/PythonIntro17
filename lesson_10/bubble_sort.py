from random import randint

# 4, 7, 2, 8, 0
# 4, 2, 7, 0, | 8
# 2, 4, 0, | 7, 8
# 2, 0, | 4, 7, 8
# 0, 2, 4, 7, 8


def bubble_sort(collection):
    count_of_iteration = 0
    for i in range(len(collection)-1):
        flag = True
        for j in range(len(collection) - i - 1):
            if collection[j] > collection[j+1]:
                collection[j], collection[j+1] = collection[j+1], collection[j]
                flag = False
        count_of_iteration += 1
        if flag:
            break
    print(count_of_iteration)


lst1 = [randint(10, 99) for _ in range(35)]
# lst1 = [15, 17, 19, 23, 23, 24, 25, 25, 32, 38, 43, 43, 44, 44, 51, 52, 57, 57, 58, 67,
# 66, 71, 71, 72, 73, 75, 75, 77, 82, 83, 83, 83, 88, 92, 93]
print('lst1 =', lst1)
bubble_sort(lst1)
print('lst1 =', lst1)


key = int(input('Please enter your key: '))
for e in lst1:
    if e == key:
        print('YES')
        break
else:
    print('NO')


def binary_search(array, key_value, left=0, right=None):
    if right is None:
        right = len(array)

    middle = (left + right) // 2
    while array[middle] != key_value and left <= right:
        if array[middle] < key_value:
            left = middle + 1
        else:
            right = middle - 1

        middle = (left + right) // 2

    return (True, middle) if not (left > right) else (False, middle+1)


flag, idx = binary_search(lst1, key)

print('Flag =', flag)
print('Index =', idx)

# if key value not found, we can insert this value by index
if not flag:
    lst1.insert(idx, key)

print(lst1)
