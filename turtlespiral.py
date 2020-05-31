import turtle as t
import time as ti
from itertools import cycle

colors = cycle(['red','orange','yellow','green','blue','purple','pink'])
#defining function for drawing
def circle(size, angle,forw):
    t.pencolor(next(colors))
    t.circle(size)
    t.right(angle)
    t.forward(forw)
    circle(size+5,angle,forw+1)

#defining canvas
t.bgcolor('black')
t.speed('fast')
t.pensize('4')
circle(20,1,2)
t1.sleep(5)
t.hideturtle()
