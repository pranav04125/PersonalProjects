import turtle as t

def tallhouse_body(length, breadth):
    t.left(90)
    t.fillcolor("green")
    t.begin_fill()

    for _ in range(2):
        t.forward(length)
        t.left(90)
        t.forward(breadth)
        t.left(90)
    
    t.end_fill()

def tallhouse_roof(length, breadth, x, y):
    t.setheading(0)
    t.fillcolor("brown")
    t.goto(0 + x, length + y)
    t.begin_fill()

    for _ in range(3):
        t.left(120)
        t.forward(breadth)
    
    t.end_fill()

def tallhouse_door(size, x, y):
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
    t.fillcolor("light grey")
    t.begin_fill()
    t.setheading(0)

    for _ in range(4):
        t.forward(side)
        t.right(90)

    t.end_fill()


def tallhouse(size = 1, x = 0, y = 0):
    length = 200 * size
    breadth = 150 * size
    window_side = 30 * size

    t.penup()
    t.goto(x, y)
    t.pendown()

    # Rectangle
    tallhouse_body(length, breadth)

    #Roof
    tallhouse_roof(length, breadth, x, y)
    
    #Door
    tallhouse_door(size, x, y)

    t.penup()
    t.goto(-130 * size + x, 150 * size + y)
    t.pendown()

    #Windows Row 1
    for i in range(3):
        tallhouse_window(window_side)
        t.penup()
        t.forward(40 * size)
        t.pendown()

    t.penup()
    t.goto(-130 * size + x, 80 * size + y)
    t.pendown()

    #Windows Row 2
    tallhouse_window(window_side)
    t.penup()
    t.forward(80 * size)
    t.pendown()
    tallhouse_window(window_side)

    t.done()

tallhouse(size=1)