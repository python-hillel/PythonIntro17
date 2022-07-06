import os
from time import sleep

height = int(input('Please enter height: '))

for line in range(height // 2):
    os.system('clear')      # cls
    for i in range(height):
        for j in range(height):
            if (
                    i == 0
                    or i == height - 1
                    or i == j
                    or j == height - i - 1
                    or (j == height // 2 and i > height // 2)
                    or (line < i < height // 2 and i <= j <= height - i - 1)
                    or (height - (line + 2) < i < height - 1 and height - 1 - i <= j <= i)
            ):
                print('* ', end='')
            else:
                print('  ', end='')
        print()
    sleep(1)
