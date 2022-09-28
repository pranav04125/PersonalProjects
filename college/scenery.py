"""This program will draw two houses, one tall and one rounch along with a tree using the turtle module."""

import turtle as t

# -----------------------------------------TREE--------------------------------------------------------------
t.pen(fillcolor="green", speed=1)

def area_rectangle(length, breadth):
    """Returns the area of a reactangle given the length and breadth"""
    return length * breadth

def draw_tree(size, x, y):
    """Draws a tree given the size and coordinates"""
    t.penup()
    t.goto(x, y)
    t.pendown()

    # begin head
    t.begin_fill()
    t.circle(size)
    size += 50
    t.end_fill()
    # end head
    # begin body
    t.fillcolor("orange")
    t.goto(10 + x, 0 + y)
    t.begin_fill()
    t.right(90)
    t.forward(size * 2)
    t.right(90)
    t.forward(15)
    t.right(90)
    t.forward(size * 2)
    t.right(90)
    t.goto(10 + x, 0 + y)
    t.end_fill()
    # end body

# -----------------------------------------TALLHOUSE--------------------------------------------------------------


def tallhouse_body(length, breadth):
    """Draws the body of the tall house"""
    t.left(90)
    t.fillcolor("light green")
    t.begin_fill()

    for _ in range(2):
        t.forward(length)
        t.left(90)
        t.forward(breadth)
        t.left(90)

    t.end_fill()


def tallhouse_roof(length, breadth, x, y):
    """Draws the roof of the tall house"""
    t.setheading(0)
    t.fillcolor("brown")
    t.goto(0 + x, length + y)
    t.begin_fill()

    for _ in range(3):
        t.left(120)
        t.forward(breadth)

    t.end_fill()


def tallhouse_door(size, x, y):
    """Draws the door if the tall house"""
    t.penup()
    t.goto(-65 * size + x, 0 + y)
    t.pendown()
    t.fillcolor("yellow")
    t.begin_fill()
    t.setheading(180)

    for _ in range(2):
        t.forward(20 * size)
        t.right(90)
        t.forward(60 * size)
        t.right(90)

    t.end_fill()


def tallhouse_window(side: int):
    """Draws a window given the side length"""
    t.fillcolor("light grey")
    t.begin_fill()
    t.setheading(0)

    for _ in range(4):
        t.forward(side)
        t.right(90)

    t.end_fill()


def tallhouse(size=1, x=0, y=0):
    """Draws a tallhouse given the size and coordinates"""

    length = 200 * size
    breadth = 150 * size
    window_side = 30 * size

    t.penup()
    t.goto(x, y)
    t.pendown()

    # Rectangle
    tallhouse_body(length, breadth)

    # Roof
    tallhouse_roof(length, breadth, x, y)

    # Door
    tallhouse_door(size, x, y)

    t.penup()
    t.goto(-130 * size + x, 150 * size + y)
    t.pendown()

    # Windows Row 1
    for i in range(3):
        tallhouse_window(window_side)
        t.penup()
        t.forward(40 * size)
        t.pendown()

    t.penup()
    t.goto(-130 * size + x, 80 * size + y)
    t.pendown()

    # Windows Row 2
    tallhouse_window(window_side)
    t.penup()
    t.forward(80 * size)
    t.pendown()
    tallhouse_window(window_side)
    return length, breadth

# -----------------------------------------ROUNCH HOUSE--------------------------------------------------------------


def houseshort(length, breadth):
    """Draws the body of the short house"""

    t.pencolor('light blue')
    t.fillcolor('light blue')
    t.begin_fill()
    t.forward(length)
    t.left(90)
    t.forward(breadth)
    t.left(90)
    t.forward(length)
    t.left(90)
    t.forward(breadth)
    t.end_fill()
    t.left(180)
    return length, breadth

def roofshort(x, y, length):
    """Draws the roof of the short house"""

    side = length // 1.73
    t.penup()
    t.goto(0 + x, 150 + y)
    t.pendown()
    t.pencolor("red")
    t.fillcolor("red")
    t.begin_fill()
    t.right(60)
    t.forward(side)
    t.right(60)
    t.forward(side)
    t.right(150)
    t.forward(length)
    t.end_fill()


def window1short(x, y):
    """Draws the window1 of the short house"""
    t.penup()
    t.goto(70 + x, 60 + y)
    t.pendown()
    t.pencolor('grey')
    t.fillcolor('grey')
    t.begin_fill()
    t.forward(40)
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(40)
    t.right(90)
    t.end_fill()


def window2short(x, y):
    """Draws the window2 of the short house"""
    t.penup()
    t.goto(270 + x, 60 + y)
    t.pendown()
    t.pencolor('grey')
    t.fillcolor('grey')
    t.begin_fill()
    t.forward(40)
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(40)
    t.right(90)
    t.end_fill()


def doorshort(x, y):
    """Draws the door of the short house"""
    t.penup()
    t.goto(170 + x, 0 + y)
    t.pendown()
    t.pencolor('brown')
    t.fillcolor('brown')
    t.begin_fill()
    t.forward(40)
    t.right(90)
    t.forward(90)
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(90)
    t.right(90)
    t.end_fill()


def shorthouse(x, y, length, breadth):
    """Draws a short house given the length breadth and coordiantes"""

    t.penup()
    t.goto(x, y)
    t.pendown()

    houseshort(length, breadth)
    roofshort(x, y, length)
    window1short(x, y)
    window2short(x, y)
    doorshort(x, y)
    return length, breadth

def main():
    """Draws a tree, shorthouse and tallhouse and prints the area of the bigger and smaller facade"""

    t.speed(10)
    draw_tree(size=60, x=200, y=170)
    
    l, b = tallhouse(size=1, x=-300, y=-45)
    area1 = area_rectangle(l, b)
    
    l, b = shorthouse(-200, -45, 300, 150)
    area2 = area_rectangle(l, b)
    
    if area1 > area2:
        print("Area of bigger facade: ", area1)
        print("Area of smaller facade: ", area2)
    else:
        print("Area of bigger facade: ", area2)
        print("Area of smaller facade: ", area1)

    print("Please close the window to end the program")
    t.done()

if __name__ == '__main__':
    main()