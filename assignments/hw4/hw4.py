import math
from graphics import Point, GraphWin, Circle, Text, Rectangle

"""
Name: <Belle Fortson>
<hw4>.py

Problem: <This program solves a number of problems, including: mouseclicks, circles, rectangles, and
information on graphics.>

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

def squares():
    width = 500
    height = 500
    win = GraphWin("square", width, height)
    click = 5
    instruction_loc = Point(width / 2, height - 10)
    instruction = Text(instruction_loc, "Click to move square")
    instruction.draw(win)

    shape = Rectangle(Point(50, 50), Point(70, 70))
    shape.setFill("red")
    shape.setOutline("red")
    shape.draw(win)
    for r in range(click):
        click_user = win.getMouse()
        shape = Rectangle(Point(click_user.x - 10, click_user.y - 10), Point(click_user.x + 10, click_user.y + 10))
        shape.setFill("red")
        shape.setOutline("red")
        shape.draw(win)
    instruction.setText("Click again to quit.")
    win.getMouse()
    win.close()


def rectangle():
    width = 500
    height = 500
    win = GraphWin("Rectangle Work", width, height)

    corner1 = win.getMouse()
    corner2 = win.getMouse()

    rectangle1 = Rectangle(corner1, corner2)
    rectangle1.draw(win)

    x1 = corner1.getX()
    x2 = corner2.getX()
    y1 = corner1.getY()
    y2 = corner2.getY()

    length = abs(x2 - x1)
    width = abs(y2 - y1)
    area = length * width
    perimeter = 2 * (length * width)
    rectangle1.setFill("green")

    text1 = Text(Point(50, 50), "The area is: " + str(area))
    text2 = Text(Point(80, 80), "The Perimeter is: " + str(perimeter))
    text1.draw(win)
    text2.draw(win)

    in_point = Point(width / 2, height - 10)
    instruction = Text(in_point, "Click again to close")
    instruction.draw(win)

    win.getMouse()
    win.close()



def circle():
    width = 400
    height = 400
    win = GraphWin("HW Circle", width, height)

    point1 = win.getMouse()
    point2 = win.getMouse()
    x1 = point1.getX()
    x2 = point2.getX()
    y1 = point1.getY()
    y2 = point2.getY()
    r = math.sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))

    circle1 = Circle(point1, r)
    circle1.draw(win)
    txt = Text(Point(100, 50), "The radius is: " + str(r))
    txt.draw(win)
    circle1.setFill("blue")

    instruct_pt = Point(width/2, height - 10)
    instructions = Text(instruct_pt, "Click again to close")
    instructions.draw(win)

    win.getMouse()
    win.close()




def pi2():
    n = eval(input("Enter the number of terms to sum: "))
    acc = 0
    for i in range (n):
        num = 4
        den = 1 + 2 * i
        frac = (num / den) * ((-1) ** i)
        acc = acc + frac

    print(acc)
    print(math.pi - acc)











