"""
Name: <Belle Fortson>
<lab6>.py

Problem: <Vigenere code creator.>

Certification of Authenticity:
<include one of the following>
I certify that this assignment is my own work, but I discussed it with: <Ben Kelehear>
"""
from graphics import *


def vigenere():
    width = 500
    height = 500
    win = GraphWin("Vigenere", width, height)
    win.setBackground("grey")

    message_loc = Point(100, 100)
    message = Text(message_loc, "Put your message here: ")
    message.draw(win)

    keyword_loc = Point(100, 150)
    keyword = Text(keyword_loc, "Enter your keyword: ")
    keyword.draw(win)

    user_entry_loc = Point(330, 100)
    user_entry = Entry(user_entry_loc, 30)
    user_entry.draw(win)

    user_key_loc = Point(330, 150)
    user_key = Entry(user_key_loc, 30)
    user_key.draw(win)

    button = Rectangle(Point(200, 200), Point(280, 250))
    button.draw(win)

    txt_pt = Point(240, 225)
    txt = Text(txt_pt, "Encode!")
    txt.draw(win)
    win.getMouse()

    acc = ""
    msg = user_entry.getText()
    msg = msg.replace(" ", "")
    msg = msg.upper()
    key = user_key.getText()
    key = key.upper()
    for j in range(len(msg)):
        msg_ord = ord(msg[j]) - 65
        key_ord = ord(key[j % len(key)]) - 65
        convert = (msg_ord + key_ord) % 26
        convert_2 = chr(convert + 65)
        acc = (acc + convert_2)

    button.undraw()
    txt.undraw()
    result_pt = Point(250, 270)
    result = Text(result_pt, "Resulting Message: ")
    conversion_pt = Point(260, 300)
    conversion = Text(conversion_pt, acc)
    conversion.draw(win)
    result.draw(win)
    close_pt = Point(250, 400)
    close_txt = Text(close_pt, "Click anywhere to close")
    close_txt.draw(win)
    win.getMouse()
    win.close()


vigenere()
