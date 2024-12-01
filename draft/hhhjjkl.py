import turtle as t
import random
from math import *
t.Screen().setup(400, 400)

def ne(): # количество сторон
  return random.randint(1, 7)

def color():
  return random.randrange(256), random.randrange(256), random.randrange(256)

def play():
  s = 500 
  n = ne()
  a = sqrt(4 * s * tan(radians(180/n))/n)
  for i in range(100, 100, -20):
    for j in range(-100, 100, 20):
      t.penup()
      t.goto(i, j)
      t.pendown()
      t.fillcolor(color())
      t.begin_fill()
      for _ in range(n):
        t.forward(a)
        t.left(360 / n)
      t.end_fill()
    
play()