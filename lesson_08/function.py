from random import randint

# [randint(10, 99) for _ in range(30)]

"""
def function_name(arg1, arg2, arg3, .... argN):
    operator1
    operator2
    operator3
    
    return
    return param
"""
# lst = [80, 57, 56, 95, 76, 97, 85, 77, 12, 75, 85, 36, 15, 27, 80, 88, 90, 87, 93, 64, 75]

lst = [randint(10, 99) for _ in range(20)]


def func_print():
    global lst
    lst = [randint(10, 99) for _ in range(10)]
    for el in lst:
        print("'" + str(el) + "'", end=' ')
    print()


def create_str(number_list):
    return ' '.join("'" + str(el) + "'" for el in number_list)


def func1(param1, param2, param3, param4=0, param5=9, param6=8):
    print(param1, param2, param3, param4, param5, param6)


def func2(*args):
    print(type(args), args)


def func3(**kwargs):
    print(type(kwargs), kwargs)


def func4(*args, **kwargs):
    print(args, kwargs)


def func5(a, b, c, d):
    res1 = a + b
    res2 = c * d
    return res1, res2


func1(1, 3, 7)
func1(1, 3, 7, 4)
func1(1, 3, 7, 4, 6)
func1(1, 3, 7, 4, 6, 2)

func2()
func2(5, 6.4, 'Hello', True)

func3()
func3(param4=12.4, param5=(9, 5.5, [4, True]), param6='Hello')

func4(5, 6.4, 'Hello', True, param4=12.4, param5=(9, 5.5, [4, True]), param6='Hello')

print(func5(2, 5, 3, 8))

func_print()
print(create_str(lst))

for i in range(len(lst)):
    lst[i] = lst[i] + 5

# func_print()
print(create_str(lst))

for i in range(len(lst)):
    lst[i] = 34 * lst[i] / 2

# func_print()
print(create_str(lst))
