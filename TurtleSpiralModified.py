import turtle as t
import time as ti
from itertools import cycle

colors = cycle(['red','orange','yellow','green','blue','purple','pink'])
#defining function for drawing
def circle(size, angle,forw, shape):
    t.pencolor(next(colors))
    next_shape = ''
    if shape == 'circle':
        t.circle(size)
        next_shape = 'square'
    elif shape == 'square':
        for i in range(4):
            t.forward(size*2)
            t.left(90)
        next_shape = 'circle'
    t.right(angle)
    t.forward(forw)
    circle(size+5,angle+1,forw+1,next_shape)

#defining canvas
t.bgcolor('black')
t.speed('fast')
t.pensize('4')
circle(30,0,1,'circle')
t1.sleep(5)
t.hideturtle()
