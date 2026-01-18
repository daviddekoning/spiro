from math import sin, cos, gcd, pi
from turtle import *

def spirocoord(r1,r2,offset,𝜗,𝜗_0=0,inside=True,x_offset=0,y_offset=0):
    """
    Returns (x, y) coordinates of the pen in a spirograph at a given
    angle theta. The periodicity of the function depends on the ratio
    r1 / r2.
    
    r1 is the diametre of the outside circle
    r2 is the diametre of the inner circle
    offset is the offset of the pen hole from the edge of the inner circle
    theta is the rotation of the inner circle around the outer circle.
    """
    𝜑 = (-1 * r1 / r2 * (𝜗) + (𝜗+𝜗_0)) % (2 * pi) 
    
    if inside:
        x = (cos(𝜗+𝜗_0) * (r1 - r2)) + (cos(𝜑) * (r2 - offset))
        y = (sin(𝜗+𝜗_0) * (r1 - r2)) + (sin(𝜑) * (r2 - offset))
    else:
        x = (cos(𝜗+𝜗_0) * (r1 + r2)) + (cos(𝜑) * (r2 - offset))
        y = (sin(𝜗+𝜗_0) * (r1 + r2)) + (sin(𝜑) * (r2 - offset))
    
    return (x+x_offset,y+y_offset)

def drange(start, stop, step):
    r = start
    while r < stop:
        yield r
        r += step

def lcm(a,b):
    return a * b / gcd(a,b)

class Spiro():
    
    def __init__(self):
        self.r1 = 105
        self.r2 = 42
        self.offset = 15
        self.theta_0 = 0
        self.color = 'black'
        self.inside = True
        self.x_offset = 0
        self.y_offset = 0
        
        self.reset()
        
    
    def draw(self):
        c = pencolor()
        color(self.color)
        pu()
        goto(spirocoord(self.r1,self.r2,self.offset,0,self.theta_0,self.inside,self.x_offset,self.y_offset))
        pd()
        for 𝛼 in drange(0,lcm(self.r1,self.r2)/self.r1*2*pi,pi/180*5):
            goto(*spirocoord(self.r1,self.r2,self.offset,𝛼,self.theta_0,self.inside,self.x_offset,self.y_offset))
        goto(spirocoord(self.r1,self.r2,self.offset,0,self.theta_0,self.inside,self.x_offset,self.y_offset))
        pu()
        goto(0,0)
        pencolor(c)

    def reset(self):
        reset()
        ht()
        speed(0)
        delay(0)
        lt(90)
        width(2)
