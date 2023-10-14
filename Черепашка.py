import turtle
x = int(input('Введите число '))
len = len(str(x))
from turtle import *
q = ('red', 'magenta', 'MediumOrchid', 'BlueViolet', 'blue', 'DodgerBlue', 'DarkTurquoise', 'lime green', 'GreenYellow', 'yellow', 'Gold', 'DarkOrange')
shape('turtle')
pensize(2)
score = 0
fxm, fym = 900, 900
try:
    while True:
        for i in q:
            if x == 1:
                begin_fill()
                for i in range(3):
                    for i in q:
                        pencolor(i)
                        if x % 2 == 1:
                            left(30)
                            forward(10)
                            x = x * 3 + 1
                            if fxm > xcor():
                                fxm = xcor()
                            if fym > ycor():
                                fym = ycor()
                        else:
                            right(30)
                            forward(10)
                            x = x / 2
                            if fxm > xcor():
                                fxm = xcor()
                            if fym > ycor():
                                fym = ycor()
                end_fill()
                hideturtle()
                speed(0)
                penup()
                setpos(fxm, fym)
                setheading(78)
                forward(46)
                FONT = ("Arial", 14)
                pencolor('red')
                pendown()
                write("Game over", font=FONT)
                exitonclick()
                print("Game over")
                print(f"Your score is {score - len}")
            else:
                pencolor(i)
                if x % 2 == 1:
                    left(30)
                    forward(10)
                    x = x * 3 + 1
                    score += 1
                else:
                    right(30)
                    forward(10)
                    x = x / 2
                    score += 1
except:
    pass
