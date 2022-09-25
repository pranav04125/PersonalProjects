import turtle

def tree():
    turtle.setheading(90)
    
    turtle.fillcolor("brown")
    turtle.begin_fill()
    turtle.forward(200)
    turtle.left(90)
    turtle.forward(10)
    turtle.left(90)
    turtle.forward(200)
    turtle.left(90)
    turtle.forward(10)
    turtle.left(90)
    turtle.end_fill()

    turtle.penup()
    turtle.forward(200)
    turtle.right(90)
    turtle.pendown()

    turtle.fillcolor("dark green")
    turtle.begin_fill()
    turtle.circle(50)
    turtle.end_fill()
    turtle.done()

tree()

import turtle as t

def window(side: int):
    t.fillcolor("light grey")
    t.begin_fill()
    t.setheading(0)
    t.forward(side)
    t.right(90)
    t.forward(side)
    t.right(90)
    t.forward(side)
    t.right(90)
    t.forward(side)
    t.end_fill()

def tallhouse(x, y, length, breadth):
    window_size = breadth // 5
    door_length = length // 3
    door_breadth = breadth // 7
    t.penup()
    t.goto(x, y)
    t.pendown()

    # Rectangle
    t.left(90)
    t.fillcolor("green")
    t.begin_fill()
    t.forward(length)
    t.left(90)
    t.forward(breadth)
    t.left(90)
    t.forward(length)
    t.left(90)
    t.forward(breadth)
    t.end_fill()

    #Triangle Roof
    t.fillcolor("brown")
    t.goto(0 + x, length + y)
    t.begin_fill()
    t.left(120)
    t.forward(breadth)
    t.left(120)
    t.forward(breadth)
    t.left(120)
    t.forward(breadth)
    t.end_fill()

    #Door
    t.penup()
    t.goto(-(breadth / 2) + door_breadth / 2 + x, 0 + y)
    t.pendown()
    t.fillcolor("yellow")
    t.begin_fill()
    t.setheading(180)
    t.forward(door_breadth)
    t.right(90)
    t.forward(door_length)
    t.right(90)
    t.forward(door_breadth)
    t.right(90)
    t.forward(door_length)
    t.end_fill()

    #Windows Row 1
    t.penup()
    t.goto(-breadth + door_breadth + x, 175 + y)
    t.pendown()
    window(window_size)
    t.penup()
    t.right(90)
    t.forward(40)
    t.pendown()
    window(window_size)
    t.penup()
    t.right(90)
    t.forward(40)
    t.pendown()
    window(window_size)

    t.penup()
    t.goto(-130 + x, 120 + y)
    t.pendown()

    #Windows Row 2
    window(window_size)
    t.penup()
    t.right(90)
    t.forward(80)
    t.pendown()
    window(window_size)

    t.done()
tallhouse(10, 20, 200, 150)