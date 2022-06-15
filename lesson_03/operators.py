"""
арифметические операторы

+----+-----------------------+--------------------------------------------------+--------------------------------------+
| +  | Сложение              | Суммирует два объекта                            | 3 + 5 даст 8; 'a' + 'b' даст 'ab'    |
+----+-----------------------+--------------------------------------------------+--------------------------------------+
| -  | Вычитание             | Даёт разность двух чисел; если первый            | -5.2 даст отрицательное число, а     |
|    |                       | операнд отсутствует, он считается равным нулю    | 50 - 24 даст 26.                     |
+----+-----------------------+--------------------------------------------------+--------------------------------------+
| *  | Умножение             | Даёт произведение двух чисел или возвращает      | 2 * 3 даст 6. 'la' * 3 даст 'lalala'.|
|    |                       | строку, повторённую заданное число раз.          |                                      |
+----+-----------------------+--------------------------------------------------+--------------------------------------+
| ** | Возведение в степень  | Возвращает число х, возведённое в степень y      | 3 ** 4 даст 81 (т.е. 3 * 3 * 3 * 3)  |
+----+-----------------------+--------------------------------------------------+--------------------------------------+
| /  | Деление               | Возвращает частное от деления x на y             | 4 / 3 даст 1.3333333333333333.       |
+----+-----------------------+--------------------------------------------------+--------------------------------------+
| // | Целочисленное деление | Возвращает неполное частное от деления           | 4 // 3 даст 1. -4 // 3 даст -2.      |
+----+-----------------------+--------------------------------------------------+--------------------------------------+
| %  | Деление по модулю     | Возвращает остаток от деления                    | 8 % 3 даст 2. -25.5 % 2.25 даст 1.5. |
+----+-----------------------+--------------------------------------------------+--------------------------------------+
"""

a = 3 ** 4 ** 5
print(a)
print(10 / 2)
print(10 / 3)
print(-4 / 3)

print(10 // 2)
print(10 // 3.)
print(-4 // 3)

print(10 % 2)
print(10 % 3)

"""
int + int = int
int + float = float

int - int = int
int - float = float

int * int = int
int * float = float

int / int = float
int / float = float

int // int = int
int // float = float
"""

"""
Операторы сравнения
+----+------------------+-------------------------------------------------------+--------------------------------------+
| <  | Меньше           | Определяет, верно ли, что x меньше y. Все операторы   | 5 < 3 даст False, а 3 < 5 даст True. |
|    |                  | сравнения возвращают True или False. Обратите         | Можно составлять произвольные цепочки|
|    |                  | внимание на заглавные буквы в этих словах.            | сравнений: 3 < 5 < 7 даёт True.      |
+----+------------------+-------------------------------------------------------+--------------------------------------+
| >  | Больше           | Определяет, верно ли, что x больше y                  | 5 > 3 даёт True. Если оба операнда - |
|    |                  |                                                       | числа, то перед сравнением они оба   |
|    |                  |                                                       | преобразуются к одинаковому типу. В  |
|    |                  |                                                       | противном случае всегда возвращается |
|    |                  |                                                       | False.                               |
+----+------------------+-------------------------------------------------------+--------------------------------------+
| <= | Меньше или равно | Определяет, верно ли, что x меньше или равно y        | x = 3; y = 6; x <= y даёт True.      |
+----+------------------+-------------------------------------------------------+--------------------------------------+
| >= | Больше или равно | Определяет, верно ли, что x больше или равно y        | x = 4; y = 3; x >= 3 даёт True.      |
+----+------------------+-------------------------------------------------------+--------------------------------------+
| == | Равно            | Проверяет, одинаковы ли значения объектов             | x = 2; y = 2; x == y даёт True.      |
|    |                  |                                                       | x = 'str'; y = 'stR'; x == y даёт    |
|    |                  |                                                       | False. x = 'str';y = 'str'; x == y   |
|    |                  |                                                       | даёт True.                           |
+----+------------------+-------------------------------------------------------+--------------------------------------+
| != | Не равно         | Проверяет, верно ли, что объекты не равны             | x = 2; y = 3; x != y даёт True.      |
+----+------------------+-------------------------------------------------------+--------------------------------------+
"""


"""
1 - True
0 - False

Логические операторы
+-----+----------------+-------------------------------------+---------------------------------------------------------+
| not | Логическое НЕ  | Если x равно True, оператор вернёт  | x = True; not x даёт False.                             |
|     |                | False. Если же x равно False,       |                                                         |
|     |                | получим True.                       |                                                         |
+-----+----------------+-------------------------------------+---------------------------------------------------------+
| and | Логическое И   | x and y даёт False, если x равно    | x = False; y = True; x and y возвращает False,          |
|     |                | False , в противном случае          | поскольку x равно False. В этом случае Python не станет |
|     |                | возвращает значение y.              | проверять значение y, так как уже знает, что левая часть|
|     |                |                                     | выражения ‘and’ равняется False, что подразумевает, что |
|     |                |                                     | и всё выражение в целом будет равно False, независимо от|
|     |                |                                     | значений всех остальных операндов. Это называется       |
|     |                |                                     | укороченной оценкой булевых (логических) выражений.     |
+-----+----------------+-------------------------------------+---------------------------------------------------------+
| or  | Логическое ИЛИ | Если x равно True, в результате     | x = True; y = False; x or y даёт True. Здесь также может|
|     |                | получим True, в противном случае    | производиться укороченная оценка выражений.             |
|     |                | получим значение y.                 |                                                         |
+-----+----------------+-------------------------------------+---------------------------------------------------------+


    A       B       and         or       not A
  True    True     True        True     False
  True    False    False       True     False
  False   True     False       True     True
  False   False    False       False    True
"""

"""
Битовые операторы
+---+-----------------------------+--------------------------------------------------------+---------------+
| & | Побитовое И                 | Побитовая операция И над числами                       | 5 & 3 даёт 1. |
+---+-----------------------------+--------------------------------------------------------+---------------+
| | | Побитовое ИЛИ               | Побитовая операция ИЛИ над числами                     | 5 | 3 даёт 7  |
+---+-----------------------------+--------------------------------------------------------+---------------+
| ^ | Побитовое ИСКЛЮЧИТЕЛЬНО ИЛИ | Побитовая операция ИСКЛЮЧИТЕЛЬНО ИЛИ                   | 5 ^ 3 даёт 6  |
+---+-----------------------------+--------------------------------------------------------+---------------+
| ~ | Побитовое НЕ                | Побитовая операция НЕ для числа x соответствует -(x+1) | ~5 даёт -6    |
+---+-----------------------------+--------------------------------------------------------+---------------+

    A       B        ^
  True    True     False
  True    False    True
  False   True     True
  False   False    False
  
    8       1000                    0111 = 7
  &                     0000                    0110
    6       0110                    0110 = 6
"""
# print(~8)

"""
Операторы сдвига
+----+--------------+-----------------------------------------------------------+--------------------------------------+
| << | Сдвиг влево  | Сдвигает биты числа влево на заданное количество позиций. | 2 << 2 даст 8. В двоичном виде 2     |
|    |              | (Любое число в памяти компьютера представлено в виде битов| представляет собой 10. Сдвиг влево на|
|    |              | или двоичных чисел, т.е. 0 и 1).                          | 2 бита даёт 1000, что вдесятичном    |
|    |              |                                                           | виде означает 8.                     |
+----+--------------+-----------------------------------------------------------+--------------------------------------+
| >> | Сдвиг вправо | Сдвигает биты числа вправо на заданное число позиций.     | 11 >> 1 даст 5. В двоичном виде 11   |
|    |              |                                                           | представляется как 1011, что будучи  |
|    |              |                                                           | смещённым на 1 бит вправо, даёт 101, |
|    |              |                                                           | а это, в свою очередь, не что иное   |
|    |              |                                                           | как десятичное 5.                    |
+----+--------------+-----------------------------------------------------------+--------------------------------------+


6 << 2          0110 << 2 = 1100 = 11000
6 >> 3          0110 >> 3 => 0011 => 0001 => 0000
"""

s = 86
x = 0
print(s & (1 << x))

"""

    01010110
    &           >   00000000
    00000100
"""


"""
Присваивание и сокращённые формы присваивания
+-----+-------------------------+----------------------------------------------------------+---------------------------+
| =   | Присвоить               | Выполняет сопоставление имени объекту в памяти.          | x = 5, y = -2.7, z = True |
|     |                         | (Устанавливает ссылку на объект)                         |                           |
+-----+-------------------------+----------------------------------------------------------+---------------------------+
| +=  | Сложение с последующим  | Выполняет сложение двух операндов и результат присваивает| x = x + 5 <==> x += 5     |
|     | присваиванием           | левому операнду оператора сложения.                      |                           |
+-----+-------------------------+----------------------------------------------------------+---------------------------+
| -=  | Вычитание с последующим | Выполняет вычитание одного операнда из другого и         | x = x - 5 <==> x -= 5     |
|     | присваиванием           | результат присваивает левому операнду оператора вычитания|                           |
+-----+-------------------------+----------------------------------------------------------+---------------------------+
| *=  | Умножение с последующим | Выполняет умножение двух операндов и результат           | x = x * 5 <==> x *= 5     |
|     | присваиванием           | присваивает левому операнду оператора умножения.         |                           |
+-----+-------------------------+----------------------------------------------------------+---------------------------+
| /=  | Деление с последующим   | Выполняет деление одного операнда на другой и результат  | x = x / 5 <==> x /= 5     |
|     | присваиванием           | присваивает левому операнду оператора деления.           |                           |
+-----+-------------------------+----------------------------------------------------------+---------------------------+
| //= | Целочисленное деление с | Выполняет деление одного операнда на другой и результат  | x = x // 5 <==> x //= 5   |
|     | последующим             | присваивает левому операнду оператора деления.           |                           |
|     | присваиванием           |                                                          |                           |
+-----+-------------------------+----------------------------------------------------------+---------------------------+
| %=  | Вычисление остатка от   | Выполняет вычисление остатка от деление одного операнда  | x = x % 5 <==> x %= 5     |
|     | деления с последующим   | на другой и результат присваивает левому операнду        |                           |
|     | присваиванием           | оператора.                                               |                           |
+-----+-------------------------+----------------------------------------------------------+---------------------------+
| **= | Возведение числа в      | Выполняет возведение числа в степень и результат         | x = x ** 5 <==> x **= 5   |
|     | степень с последующим   | присваивает левому операнду оператора возведения.        |                           |
|     | присваиванием           |                                                          |                           |
+-----+-------------------------+----------------------------------------------------------+---------------------------+
| >>= | Сдвиг битов числа вправо| Выполняет сдвиг битов числа вправо и результат           | x = x >> 5 <==> x >>= 5   |
|     | с последующим           | присваивает левому операнду оператора сдвига.            |                           |
|     | присваиванием           |                                                          |                           |
+-----+-------------------------+----------------------------------------------------------+---------------------------+
| <<= | Сдвиг битов числа влево | Выполняет сдвиг битов числа влево и результат присваивает| x = x << 5 <==> x <<= 5   |
|     | с последующим           | левому операнду оператора сдвига.                        |                           |
|     | присваиванием           |                                                          |                           |
+-----+-------------------------+----------------------------------------------------------+---------------------------+
| &=  | Выполняется битовое 'И' | Выполняется операция битовое 'И' и результат присваивает | x = x & y <==> x &= y     |
|     | с последующим           | левому операнду оператора 'И'.                           |                           |
|     | присваиванием           |                                                          |                           |
+-----+-------------------------+----------------------------------------------------------+---------------------------+
| |=  | Выполняется битовое     | Выполняется операция битовое 'ИЛИ' и результат           | x = x | y <==> x |= y     |
|     | 'ИЛИ' с последующим     | присваивает левому операнду оператора 'ИЛИ'.             |                           |
|     | присваиванием           |                                                          |                           |
+-----+-------------------------+----------------------------------------------------------+---------------------------+
| ^=  | Выполняется битовое     | Выполняется операция битовое 'Исключающее ИЛИ' и         | x = x ^ y <==> x ^= y     |
|     | 'Исключающее ИЛИ' с     | результат присваивает левому операнду оператора          |                           |
|     | последующим             | 'Исключающее ИЛИ'.                                       |                           |
|     | присваиванием           |                                                          |                           |
+-----+-------------------------+----------------------------------------------------------+---------------------------+
"""


"""
5       -5
a = 5
b = -a
"""