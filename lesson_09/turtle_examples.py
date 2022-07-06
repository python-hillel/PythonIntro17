# import turtle
# from time import sleep
#
# pen = turtle.Pen()
# for x in range(100):
#     pen.forward(x)
#     pen.left(90)
#
# sleep(5)


# import turtle
# from time import sleep
#
#
# pen = turtle.Pen()
# for x in range(100):
#     pen.forward(x)
#     pen.left(91)
#
# sleep(5)

# import turtle
# from time import sleep
#
#
# pen = turtle.Pen()
# for x in range(100):
#     pen.circle(x)
#     pen.left(91)
#
# sleep(5)

import turtle

colors = [
    'red',
    'purple',
    'blue',
    'green',
    'yellow',
    'orange',
]

t = turtle.Pen()
turtle.bgcolor('black')
for x in range(360):
    t.pencolor(colors[x % 6])
    t.width(int(x / 100 + 1))
    t.forward(x)
    t.left(59)