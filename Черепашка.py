import turtle

x = int(input('Введите число '))
from turtle import *
q = ('red', 'magenta', 'MediumOrchid', 'BlueViolet', 'blue', 'DodgerBlue', 'DarkTurquoise', 'lime green', 'GreenYellow', 'yellow', 'Gold', 'DarkOrange')
shape('turtle')
pensize(2)
f = 10
while True:
    for i in q:
        pencolor(i)
        if x % 2 == 1:
            left(30)
            forward(f)
            x = x * 3 + 1
        else:
            right(30)
            forward(f)
            x = x / 2
# 657187189415641

from turtle import *
pensize(2)
speed(15)
# ****
exitonclick()