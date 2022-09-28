import math
import turtle as t
import time

def draw_rectangle(length, breadth):
    for _ in range(2):
        t.forward(length)
        t.left(90)
        t.forward(breadth)
        t.left(90)

def draw_isosceles(base, vertical_height=0, angle_pair=0):
    if vertical_height == 0 and angle_pair == 0:
        return 0
    
    if angle_pair == 0:
        side = math.sqrt(((base/2)**2) + vertical_height**2)
        angle_pair = math.asin((vertical_height/side))  * (180/math.pi)
    else:
        if angle_pair >= 90 and angle_pair <= 0:
            return

        side = (base/2) / math.cos(angle_pair * math.pi/180)
        print(side)

    t.forward(base)
    t.left(180 - angle_pair)
    t.forward(side)
    t.left(2 * angle_pair)
    t.forward(side)
    t.left(180 - angle_pair)

def draw_house(length, breadth, vertical_height=0, angle_pair=0):
    draw_rectangle(length, breadth)
    
    t.penup()
    t.left(90)
    t.forward(breadth)
    t.right(90)
    t.pendown()

    base = length
    draw_isosceles(base, vertical_height, angle_pair)

def draw_tree(height, diameter):
    for _ in range(3):
        t.forward(15)
        t.left(90)
        t.forward(height)
        t.left(90)

    t.forward(7.5)
    t.setheading(0)
    t.circle(diameter/2)

def test_code():
    """for testing purposes"""

    draw_rectangle(300, 250)
    time.sleep(2)
    t.clear()
    t.home()

    draw_isosceles(100, vertical_height=200)
    time.sleep(2)
    t.clear()
    t.home()

    draw_isosceles(100, angle_pair=30)
    time.sleep(2)
    t.clear()
    t.home()
    t.home()

    draw_house(300, 200, 150)
    time.sleep(2)
    t.clear()
    t.home()

    draw_tree(200, 150)

    t.penup()
    t.home()
    t.pendown()

    t.done()

test_code()