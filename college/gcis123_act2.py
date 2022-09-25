import turtle as t

# -----------------------------------------TREE--------------------------------------------------------------
t.pen(fillcolor="green", speed=1)


def draw_tree(size, x, y):
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


def tallhouse(size=1, x=0, y=0):
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

# -----------------------------------------ROUNCH HOUSE--------------------------------------------------------------


def houseshort():
    t.pencolor('light blue')
    t.fillcolor('light blue')
    t.begin_fill()
    t.forward(300)
    t.left(90)
    t.forward(150)
    t.left(90)
    t.forward(300)
    t.left(90)
    t.forward(150)
    t.end_fill()
    t.left(180)


def roofshort(x, y):
    t.penup()
    t.goto(0 + x, 150 + y)
    t.pendown()
    t.pencolor("red")
    t.fillcolor("red")
    t.begin_fill()
    t.right(60)
    t.forward(173)
    t.right(60)
    t.forward(173)
    t.right(150)
    t.forward(300)
    t.end_fill()


def window1short(x, y):
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


def shorthouse(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

    houseshort()
    roofshort(x, y)
    window1short(x, y)
    window2short(x, y)
    doorshort(x, y)

def main():
    t.speed(10)
    draw_tree(size=60, x=200, y=170)
    tallhouse(size=1, x=-300, y=-45)
    shorthouse(-200, -45)
    t.done()

if __name__ == '__main__':
    main()