from turtle import *
from random import *
shape('arrow')
speed(0)
colors = ['red', 'blue', 'green', 'black', 'yellow']
lenos = [20, 40, 60, 80, 100]
dist = [[0, 0], [100, 100], [-100, -100], [-100, 100], [100, -100]]
for i in range(5):
  le = choice(lenos)
  col = choice(colors)
  penup()
  m = choice(dist)
  goto(m)
  pendown()
  for j in range(8):
    pencolor(col)
    forward(le)
    left(180)
    n = 4
    while n != 0:
      forward(le / 4)
      right(120)
      forward(le // 7)
      backward(le // 7)
      right(120)
      forward(le // 7)
      backward(le // 7)
      right(120)
      n -= 1
    left(180)
    left(45)
  del lenos[lenos.index(le)]
  del colors[colors.index(col)]
  del dist[dist.index(m)]