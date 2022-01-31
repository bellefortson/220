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
    sum1 = 0
    upper = eval(input("What is the Upper Bound? "))
    for i in range(0, upper + 1, 3):
        sum1 = sum1 + i

    print("The sum of threes is: ", sum1)

def multiplication_table():
    for i in range(1, 11):
        for j in range(1, 11):
            print(str(i*j), end="\t")
        print()




def triangle_area():
    side_a = eval(input("enter the length of side a: "))
    side_b = eval(input("enter the length of side b: "))
    side_c = eval(input("enter the length of side c: "))

    side = (side_a + side_b + side_c) / 2
    area = math.sqrt(side * (side - side_a) * (side - side_b) * (side - side_c))
    print("The area is: ", area)


#  triangle_area()


def sum_squares():
    square = 0
    lower = eval(input("What is the Lower Bound? "))
    upper = eval(input("What is the Upper Bound? "))
    for i in range(lower, upper+1):
        square = square + (i * i)

        # sum_squares = (sum_squares * sum_squares) + (sum_squares + 1)
    print("The sum of squares is: ", square)

# sum_squares()


def power():
    base = eval(input("Enter the base: "))
    exponent = eval(input("Enter the exponent: "))
    result = 1
    for _ in range(exponent):
        result = result * base
    print(result)
# I emailed regarding my issues and questions with this problem.

if __name__ == '__main__':
    pass
