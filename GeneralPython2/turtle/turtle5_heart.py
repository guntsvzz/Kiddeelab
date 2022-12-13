import turtle as t
import math

def draw_heart(alpha,d):
    t.fillcolor('red')
    r = d/math.tan(math.radians(180-alpha/2))
    t.up()
    t.goto(0,-d*math.cos(math.radians(45)))
    t.seth(90-(alpha-180))
    t.down()
    t.begin_fill()
    t.fd(d)
    t.circle(r,alpha)
    t.left(180)
    t.circle(r,alpha)
    t.fd(d)
    t.end_fill()
    t.done()

draw_heart(220,100)