from graphics import Point, GraphWin, Polygon, Text
import time


def valentine():
    width = 500
    height = 500
    win = GraphWin("Hearts", width, height)
    # text
    words_loc = Point(width / 2, height - 30)
    words = Text(words_loc, "Happy Valentine's Day!")
    # heart
    heart = Polygon(Point(250, 400), Point(100, 150), Point(120, 120), Point(160, 100), Point(250, 160),
                    Point(340, 100), Point(380, 120), Point(400, 150))
    heart.setFill("red")
    # arrow
    arrow_x = 50
    arrow_y = 50
    arrow1 = Polygon(Point(arrow_x, (arrow_y + 350)), Point((arrow_x - 5), (arrow_y + 340)),
                     Point((arrow_x + 350), arrow_y), Point((arrow_x + 340), (arrow_y - 5)))
    arrow2 = Polygon(Point((arrow_x + 360), (arrow_y + 5)), Point((arrow_x + 330), (arrow_y - 5)),
                     Point((arrow_x + 350), (arrow_y - 15)))
    arrow1.setFill("black")
    arrow2.setFill("black")
    win.setBackground("pink")
    arrow1.draw(win)
    arrow2.draw(win)
    words.draw(win)
    heart.draw(win)
    for _ in range(40):
        arrow1.move(5, -5)
        arrow2.move(5, -5)
        time.sleep(.5)

    in_point = Point(width / 2, height - 10)
    instruction = Text(in_point, "Click again to close")
    instruction.draw(win)

    win.getMouse()
    win.close()


valentine()
