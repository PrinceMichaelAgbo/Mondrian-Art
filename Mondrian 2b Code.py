# ----------------------------------------------------------
# --------      Recursive Mondrian Art: Fall Theme ------
# ----------------------------------------------------------

# ----------------------------------------------------------
# Prince Michael Agbo
# ----------------------------------------------------------

import turtle
import random

WIDTH = 1024
HEIGHT = 768


def mondrian(x, y, w, h, t):
    """
       This function calls the function to draw the initial rectangle and
       the function that will be recursed.
    """
    draw_rectangle(x,y,w,h,t)#draws the initial rectangle
    conditions(x,y,w,h,t)#this is the recursive function

def moveturtle(x,y,t):
    """
       This function moves the turtle to the coordinates (x,y)
       without leaving a line trail.
    """
    t.penup()
    t.goto(x,y)
    t.pendown()

def draw_rectangle(x,y,width,height,t):
    """
       This function starts and ends at coordinate(x,y) by
       drawing a rectangle of width w and height h.
    """
    moveturtle(x,y,t)
    for draw in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)
    

def MapleLeaf2(x, y, scale, t):
    def my_goto(x_offset, y_offset):
        t.goto(x + scale*x_offset, y + scale*y_offset)

    loc = [(5, -4), (4, -3), (9, 1), (7, 2), (8, 5), (5, 4),
           (5, 5), (3, 4), (4, 9), (2, 7), (0, 10), (-2, 7),
           (-4, 8), (-3, 3), (-5, 6), (-5, 4), (-8, 5), (-7, 2),
           (-9, 1), (-4, -3), (-5, -4), (0, -3), (2, -7), (2, -6), (1, -3)]
    for locs in loc:
           my_goto(locs[0], locs[1])


def conditions(x,y,w,h,t):
    """
       This function determines the horizontal and vertical split points,
       and uses the appropriate conditions(if statements) to determine
       how the rectangle of width w and height h will be split.
    """
    splitpoint_w = random.uniform((1/4)*w, (3/4)*w)#determine the point along the width where vertical splitting will occur
    splitpoint_h = random.uniform((1/4)*h,(3/4)*h)#determine the point along the height where horizontal splitting will occur
    
    if w > WIDTH/2 and h > HEIGHT/2:
        split_four(x,y,w,h,t,splitpoint_w,splitpoint_h)#split into four rectangles
    elif w > WIDTH/2:
        split_vertically(x,y,w,h,t,splitpoint_w,splitpoint_h)#split into two rectangles, vertically
    elif h > HEIGHT/2:
        split_horizontally(x,y,w,h,t,splitpoint_w,splitpoint_h)#split into two rectangles, horizontally
    elif split_condition(w,h) == "Both":
        split_four(x,y,w,h,t,splitpoint_w,splitpoint_h)
    elif split_condition(w,0) == "w_split":
        split_vertically(x,y,w,h,t,splitpoint_w,splitpoint_h)
    elif split_condition(0,h) == "h_split":
        split_horizontally(x,y,w,h,t,splitpoint_w,splitpoint_h)
    else:
        region_color(t)#determine the fill color
        t.begin_fill()
        draw_rectangle(x,y,w,h,t)#draw the rectangle to be colored
        t.end_fill()

        moveturtle(x+w/2, y+h/2, t)
        t.pensize(1)
        t.fillcolor(random.choice(["red", "chocolate", "orange", "brown", "chocolate"]))
        t.begin_fill()
        MapleLeaf2(x+w/2, y+h/2, 2, t)
        t.end_fill()
        t.pencolor("white")
        t.pensize(3)
        t.goto(x, y)
        t.pensize(5)
        t.pencolor("black")
        
        #moveturtle(x,y,t)
        
        
def split_four(x,y,w,h,t,splitpoint_w,splitpoint_h):
    """
       This function splits the current rectangle of width w and height h into
       four smaller rectangles and recurses for each smaller rectangle.
    """
    t.pensize(5)
    #for below, draw four rectangles to mimic splitting
    draw_rectangle(x+splitpoint_w,y,w-splitpoint_w,splitpoint_h,t)#bottom right
    draw_rectangle(x,y,splitpoint_w,splitpoint_h,t)#bottom left 
    draw_rectangle(x,y+splitpoint_h,splitpoint_w,h-splitpoint_h,t)#topleft
    draw_rectangle(x + splitpoint_w,y+splitpoint_h,w-splitpoint_w,h-splitpoint_h,t)#topright

    #For below, recurse on each smaller rectangle
    conditions(x+splitpoint_w,y,w-splitpoint_w,splitpoint_h,t)#bottom right
    conditions(x,y,splitpoint_w,splitpoint_h,t)#bottom left
    conditions(x,y+splitpoint_h,splitpoint_w,h-splitpoint_h,t)#topleft
    conditions(x + splitpoint_w,y+splitpoint_h,w-splitpoint_w,h-splitpoint_h,t)#topright

def split_vertically(x,y,w,h,t,splitpoint_w,splitpoint_h):
    """
       This function vertically splits the current rectangle of
       width w and height h into two smaller rectangles and recurses for
       each smaller rectangle.
    """
    t.pensize(3)
    #for below, draw two rectangles, left and right, to mimic splitting
    draw_rectangle(x,y,splitpoint_w,h,t)#left
    draw_rectangle(x+splitpoint_w,y,w-splitpoint_w,h,t)#right

    #For below, recurse on each smaller rectangle
    conditions(x,y,splitpoint_w,h,t)#left
    conditions(x+splitpoint_w,y,w-splitpoint_w,h,t)#right

def split_horizontally(x,y,w,h,t,splitpoint_w,splitpoint_h):
    """
       This function horizontally splits the current rectangle of
       width w and height h into two smaller rectangles and recurses for
       each smaller rectangle.
    """
    t.pensize(1)
    #for below, draw two rectangles, top and bottom, to mimic splitting
    draw_rectangle(x,y+splitpoint_h,w,h-splitpoint_h,t)#top
    draw_rectangle(x,y,w,splitpoint_h,t)#bottom

    #For below, recurse on each smaller rectangle
    conditions(x,y+splitpoint_h,w,h-splitpoint_h,t)#top
    conditions(x,y,w,splitpoint_h,t)#bottom
    
def split_condition(w,h):
    """
       This function decides if the rectangle of width w and height h
       will be split or not, and if it will be done vertically,
       horizontally or both.
    """
    
    if w != 0:
        tosplit_w = random.uniform(120, w*1.5)
    if h != 0:
        tosplit_h = random.uniform(120, h*1.5)
    if w != 0 and h != 0:#if we want to split vertically and horizontally
        if tosplit_w < w and tosplit_h < h:
            return "Both"
    elif w != 0:#If we want to split vertically
        if tosplit_w < w:
            return "w_split"
    elif h!=0:#if we want to split horizontally
        if tosplit_h < h:
            return "h_split"

def region_color(t):
    """
       This function randomly decides the turtle fill color.
    """
    r = random.random()
    if r < 0.2:
        t.fillcolor("red")
    elif r < 0.4:
        t.fillcolor("green")
    elif r < 0.6:
        t.fillcolor("yellow")
    elif r < 0.8:
        t.fillcolor("brown")
    else: #r < 0.5:
        t.fillcolor("orange")
    #else:
        #t.fillcolor("white")
        
def main():
    # Create a window with a canvas
    wn = turtle.Screen()
    wn.setworldcoordinates(0, 0, WIDTH+1, HEIGHT+1)
    t = turtle.Turtle()
    t.pensize(5)
    t.speed(500)
    #t.hideturtle()

    # Draw the art
    mondrian(0, 0, WIDTH, HEIGHT, t)
    moveturtle(WIDTH/2, HEIGHT/2, t)
    t.fillcolor(random.choice(["red", "chocolate", "orange", "brown", "green"]))
    t.begin_fill()
    MapleLeaf2(WIDTH/2, HEIGHT/2, 10, t)
    t.end_fill()
    
    wn.exitonclick()

if __name__ == '__main__':
    main()

