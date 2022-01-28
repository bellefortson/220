"""
Name: <Belle Fortson>
<hw2>.py

Problem: <This assignment solves various mathematical problems.
 I have emailed about my issues and questions with this assignment,
  and would greatly appreciate any help>

Certification of Authenticity:

I certify that this assignment is entirely my own work.

"""
import math


def sum_of_threes():
    pass
# I emailed regarding my issues and questions with this problem.

def multiplication_table(a, b):
    for x in range(a, (b + 1)):
        for y in range(a, (b + 1)):
            print(str(x*y), end="\t")
        print()


multiplication_table(1, 10)

def triangle_area():
    a = eval(input("enter the length of side a: "))
    b = eval(input("enter the length of side b: "))
    c = eval(input("enter the length of side c: "))

    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    print("The area is: ", area)


triangle_area()


def sum_squares():

    # lower = eval(input("Enter the Lower Range: "))
    # upper = eval(input("Enter the Upper Range: "))
    # for i in range(lower, upper):
    #    square = i * i
    #    sum_square = square + square + square
   # print(sum_square)
# I emailed regarding my issues and questions with this problem.
sum_squares()


def power():
    pass
# I emailed regarding my issues and questions with this problem.

if __name__ == '__main__':
    pass
