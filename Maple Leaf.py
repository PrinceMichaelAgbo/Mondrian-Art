import turtle

def MapleLeaf2(x, y, scale):
    def my_goto(x_offset, y_offset):
        turtle.goto(x + scale*x_offset, y + scale*y_offset)

    turtle.penup()
    my_goto(1, -3)
    turtle.pendown()
    loc = [(5, -4), (4, -3), (9, 1), (7, 2), (8, 5), (5, 4),
           (5, 5), (3, 4), (4, 9), (2, 7), (0, 10), (-2, 7),
           (-4, 8), (-3, 3), (-5, 6), (-5, 4), (-8, 5), (-7, 2),
           (-9, 1), (-4, -3), (-5, -4), (0, -3), (2, -7), (2, -6), (1, -3)]
    for locs in loc:
           my_goto(locs[0], locs[1])
           
    

def MapleLeaf(x=None,y=None):
    if x==None:
        x=0
    if y==None:
        y=0
    turtle.penup()
    turtle.goto(1+x,-3+y)
    turtle.pendown()
    turtle.goto(5+x,-4+y)
    turtle.goto(4+x,-3+y)
    turtle.goto(9+x,1+y)
    turtle.goto(7+x,2+y)
    turtle.goto(8+x,5+y)
    turtle.goto(5+x,4+y)
    turtle.goto(5+x,5+y)
    turtle.goto(3+x,4+y)
    turtle.goto(4+x,9+y)
    turtle.goto(2+x,7+y)
    turtle.goto(0+x,10+y)
    turtle.goto(-2+x,7+y)
    turtle.goto(-4+x,8+y)
    turtle.goto(-3+x,3+y)
    turtle.goto(-5+x,6+y)
    turtle.goto(-5+x,4+y)
    turtle.goto(-8+x,5+y)
    turtle.goto(-7+x,2+y)
    turtle.goto(-9+x,1+y)
    turtle.goto(-4+x,-3+y)
    turtle.goto(-5+x,-4+y)
    turtle.goto(0+x,-3+y)
    turtle.goto(2+x,-7+y)
    turtle.goto(2+x,-6+y)
    turtle.goto(1+x,-3+y)
    turtle.hideturtle()


turtle.pencolor("black")
turtle.fillcolor("brown")

for i in range (0, 300, 100):
    for j in range(0, 300, 100):
        turtle.begin_fill()
        MapleLeaf2(i,j,2)
        turtle.end_fill()

