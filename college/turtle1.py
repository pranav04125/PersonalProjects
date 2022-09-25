import turtle


t = turtle.Turtle()

# for background
screen = turtle.Screen()
screen.bgcolor("beige")

#color and speed
# of turtle
# creating the house
t.color("black")
t.shape("turtle")
t.speed(10)


t.fillcolor('DarkSalmon')
t.begin_fill( )
t.right(90)
t.forward(160)
t.left(90)
t.forward(200)
t.left(90)
t.forward(160)
t.left(90)
t.forward(200)
t.right(90)
t.end_fill()

t.fillcolor('coral4')
t.begin_fill()
t.right(40)
t.forward(150)
t.right(98)
t.forward(155)
t.end_fill()


t.right(90)
t.penup()
t.forward(130)
t.setheading(180)
t.forward(50)
t.pendown()
t.fillcolor('bisque')
t.begin_fill()
for i in range(4):
	t.forward(45)
	t.left(90)
t.end_fill()

t.penup()
t.right(90)
t.forward(50)
t.pendown()
t.fillcolor('bisque')
t.begin_fill()
t.left(90)
for i in range(4):
	t.forward(45)
	t.left(90)
t.end_fill()

t.right(180)
t.penup()
t.forward(120)
t.right(90)
t.pendown()

t.fillcolor('CadetBlue2')
t.begin_fill()
t.forward(125)
t.right(90)
t.forward(65)
t.right(90)
t.forward(125)
t.right(90)
t.forward(65)
t.end_fill()

t.left(180)
t.penup()
t.forward(550)
t.right(90)
t.forward(60)
t.left(180)
t.pendown()

t.fillcolor('CornFlowerBlue')
t.begin_fill( )
t.forward(200)
t.left(90)
t.forward(200)
t.left(90)
t.forward(200)
t.left(90)
t.forward(200)
t.right(90)
t.end_fill()

t.fillcolor('cornsilk2')
t.begin_fill()
t.right(40)
t.forward(150)
t.right(98)
t.forward(155)
t.end_fill()

t.right(90)
t.penup()
t.forward(130)
t.setheading(180)
t.forward(50)
t.pendown()
t.fillcolor('bisque')
t.begin_fill()
for i in range(4):
	t.forward(50)
	t.left(90)
t.end_fill()

t.penup()
t.right(90)
t.forward(60)
t.pendown()
t.fillcolor('bisque')
t.begin_fill()
t.left(90)
for i in range(4):
	t.forward(50)
	t.left(90)
t.end_fill()

t.right(180)
t.penup()
t.forward(120)
t.right(90)
t.pendown()

t.fillcolor('azure2')
t.begin_fill()
t.forward(160)
t.right(90)
t.forward(65)
t.right(90)
t.forward(160)
t.right(90)
t.forward(65)
t.end_fill()

t.left(180)
t.penup()
t.forward(250)
t.left(90)
t.forward(200)
t.right(90)
t.forward(60)
t.right(180)
t.pendown() 

def drawRectangle(t, width, height, color):
    t.fillcolor(color)
    t.begin_fill()
    t.forward(width)
    t.left(90)
    t.forward(height)
    t.left(90)
    t.forward(width)
    t.left(90)
    t.forward(height)
    t.left(90)
    t.end_fill()

drawRectangle(t, 40, 150, "brown")

t.penup()
t.left(90)
t.forward(150)
t.right(90)
t.forward(24)
t.pendown()

def circle(r):
    t.fillcolor("DarkOliveGreen4")
    t.begin_fill()
    t.circle(r)
    t.end_fill()

circle(90)

t.penup()
t.goto(330,-200)
t.pendown()
drawRectangle(t, 40, 150, "brown")
t.penup()
t.left(90)
t.forward(150)
t.right(90)
t.forward(24)
t.pendown()
circle(90)
turtle.done()