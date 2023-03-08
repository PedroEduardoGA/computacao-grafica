import math
import matplotlib.pyplot as plot

def putPixel(x, y):
    plot.scatter(x, y)

def DDA(x1, y1, x2, y2):
    step = math.fabs(x2-x1)

    if(math.fabs(y2-y1) > step):
        step = math.fabs(y2-y1)

    xinc = (x2-x1) / step
    yinc = (y2-y1) / step

    x = x1
    y = y1

    while(x < x2):
        putPixel(x, y)
        x = x+xinc
        y = y+yinc

def bresenham(x1, y1, x2, y2):
    dx = x2-x1
    dy = y2-y1
    p = 2*dy - dx
    p2 = 2*dy
    xy2 = 2*(dy-dx)

    x = x1
    y = y1
    putPixel(x, y)

    while(x < x2):
        x+=1

        if(p < 0):
            p+=p2
        else:
            y+=1
            p+=xy2

        putPixel(x, y)
