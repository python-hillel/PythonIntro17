# 2 ^ 5 = 2 * 2 * 2 * 2 * 2
# 2 ^ 5 ===> 2 * (2 ^ 4) ===> 2 * (2 ^ 3) ===> 2 * (2 ^ 2) ===> 2 * (2 ^ 1) ===> 2 * (2 ^ 0)
# 32 <=== 2 * 16 <=== 2 * 8 <=== 2 * 4 <=== 2 * 2 <=== 2 * 1


def iteratively_pow(num, exp):
    res = 1
    while exp > 0:
        res *= num
        exp -= 1

    return res


print(iteratively_pow(2, 5))


def recursive_pow(num, exp):
    # base case
    if exp == 0:
        return 1

    # recursive case
    return num * recursive_pow(num, exp - 1)


print(recursive_pow(2, 5))

#                        10
# 0 1 1 2 3 5 8 13 21 34 55


def fibb_iter(num):
    x0 = 0
    x1 = 1
    while num > 0:
        res = x0 + x1
        x0 = x1
        x1 = res
        num -= 1
    return x0


print(fibb_iter(10))


def fibb_rec(num):
    # if 0 <= num <= 1:
    #     return num

    # return fibb_rec(num-1) + fibb_rec(num-2)
    return num if 0 <= num <= 1 else fibb_rec(num-1) + fibb_rec(num-2)


print(fibb_rec(10))

