hoeken = int(input('Hoeveel hoeken?: '))

import turtle

t = turtle.Turtle()
s = turtle.Screen()

def polygon(n):
    turn = 360 / n
    for sides in range(0, n, 1):
        t.forward(100)
        t.left(turn)
   # turtle.done()
    print('done!')

polygon(hoeken)
turtle.done()