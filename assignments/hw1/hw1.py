"""
Name: <Belle Fortson>
<hw1>.py

Problem: <This program solves a number of problems, including: area, volume, shooting percentage, coffee prices,
and kilometers to miles.>

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def calc_rec_area():
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the width: "))
    area = length * width
    print("Area =", area)


calc_rec_area()


def calc_volume():
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the width: "))
    height = eval(input("Enter the height: "))
    volume = length * width * height
    print("Volume =", volume)


calc_volume()


def shooting_percentage():
    shots = eval(input("Enter the player's total shots: "))
    score = eval(input("Enter how many shots the player made: "))
    percentage = score/shots
    print("Shooting Percentage =", percentage)


shooting_percentage()


def coffee():
    pounds = eval(input("How many pounds of coffee would you like? "))
    total = (pounds * 10.50) + (pounds * .86) + 1.50
    print("Your total is : ", total)


coffee()


def kilometers_to_miles():
    kilometers = eval(input("How many kilometers did you travel? "))
    total = kilometers * 0.6214
    print("That's", total, "miles!")


kilometers_to_miles()


if __name__ == '__main__':
    pass
