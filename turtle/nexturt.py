import turtle
from turtle import *

length = 0

def square():
    forward(length)
    right(90)

v = True

while v == True:
    for i in range(4):
        square()
    right(5)
    length +=5

    if length == 250:
        v = False
