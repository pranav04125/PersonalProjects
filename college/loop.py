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