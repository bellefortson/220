"""
Name: <Belle Fortson>
<hw3>.py

Problem: < This assignment worked to solve averages, tips, Newton's law,
and different sequences.>

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def average():
    num = eval(input("How many grades will you enter? "))
    avg1 = 0
    for _ in range(num):
        value = eval(input("Enter grade: "))
        avg1 = avg1 + value
    final_average = avg1 / num
    print("The average is: ",  final_average)


def tip_jar():
    final_tip = 0
    for _ in range(1, 6):
        tip = eval(input("How much would you like to donate? "))
        final_tip = final_tip + tip

    print("Total tips: ", final_tip)


def newton():

    square = eval(input("What number do you want to square root? "))
    improve = eval(input("How many times should we improve the approximation? "))
    approx = square
    for _ in range(improve):
        approx = (approx + square / approx) / 2

    print("The square root is approximately ", approx)


def sequence():
    num = int(input("How many Terms Would You Like? "))
    for i in range(num):
        list1 = (i + 1) % 2
        print(i + list1, end=" ")


def pi():
    number_term = eval(input("How many terms in the series?"))
    acc = 1
    for i in range(number_term):
        numerator = i + (2.0 - (i % 2.0))
        denom = i + (1.0 + (i % 2.0))
        acc = acc * (numerator/denom)
    final_pi = acc * 2.0
    print(final_pi)


if __name__ == '__main__':
    pass
