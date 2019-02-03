import turtle
from turtle import *

t = turtle.Turtle()
t.speed(10)

sides = int(input('please enter how many sides you want: '))

def triangle(sidenum):
    x = 360/sidenum
    for i in range(sidenum):
        forward(10)
        right(x)

triangle(sides)
