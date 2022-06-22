from string import ascii_uppercase as au

print(chr(0x1F602))
print(chr(128514))
print('\U0001f602')            # u - 2b         U - 4b

print(ord('😂'))
print(hex(ord('😂')))

wave = '~'
boat = '\U0001F6A3'
seagull = '\u033C'
fish = '\U0001F41F'
penguin = '\U0001F427'
wale = '\U0001F40B'
octopus = '\U0001F419'

seagull_row = wave * 15 + seagull + wave * 12 + '\n'
row = wave * 10 + boat + wave * 15 + '\n'
fish_row = wave * 4 + fish + wave * 21 + '\n'
wale_row = wave * 10 + wale + wave * 15 + '\n'
penguin_row = wave * 7 + penguin + wave * 18 + '\n'
octopus_row = wave * 17 + octopus + wave * 8 + '\n'

sea = seagull_row + row + fish_row + wale_row + penguin_row + octopus_row
print(sea)
print(len(sea))

# s = input('Введите строку: ')
# print(s)
# print(len(s))

# []
#               0   1   2   3   4
#               H   E   L   L   O
#              -5  -4  -3  -2  -1

s = 'finished'
print(s[0])
print(s[len(s)-1])
print(s[-1])

# slice
# string[start : stop : step]
# string[:]

print(au)
print(au[0:4])
print(au[:4])
print(au[-4:])
print(au[::2])
print(au[::-1])

print(au[:9476528972659847365928365987])
print(au[-345345435435:])

s = 'process finIshEd with exit coDe 0 ProCess finished With exit code 0 Process finished with exit code 0'
# Methods
# str.find(sub_str, start, end)
# str.rfind(sub_str, start, end)
print(s.find('e'))
print(s.find('e', 5))
print(s.find('e', 15))
print(s.find('e', 23))
print(s.find('e', 31))

print(s.find('cess'))
print(s.find('cess', 4))
print(s.find('cess', 38))
print(s.find('cess', 72))

# str.replace(old, new, count)
print(s.replace('cess', 'WWWWWWW', 2))

# str.count(sub_str)
print(s.count('WWW'))

# str.capitalize()
print(s.capitalize())

# str.title()
print(s.title().replace(' ', ''))

# str.upper()
# str.lower()
print(s.upper())
print(s.lower())

ss = '    AAAAAAAProcess finished withBBBBBB         '
# str.strip(sub_str)
# str.lstrip(sub_str)
# str.rstrip(sub_str)
print("'" + ss + "'")
print("'" + ss.strip(' AB') + "'")

# str.split(sub_str)
# str_div.join(list)
