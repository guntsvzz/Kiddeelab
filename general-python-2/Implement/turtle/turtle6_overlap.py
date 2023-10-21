import turtle
import math

screen = turtle.Screen()
screen.title('N Overlapping Circles')
screen.setup(1000,1000)
turtle.hideturtle()
turtle.speed(0)
turtle.pensize(2)

def draw_circle(x,y,radius):
  turtle.up()
  turtle.goto(x,y-radius)
  turtle.seth(0)
  turtle.down()
  turtle.circle(radius,steps=360)

r = 150
n = 10
r2 = r/2/math.sin(math.radians(180/n))
angle = 90
for _ in range(n):
    draw_circle(r2*math.cos(math.radians(angle)),
                r2*math.sin(math.radians(angle)),
                r)
    angle += 360/n
turtle.done()
