from math import pi
"""
Name: <Belle Fortson>
<hw6>.py

Problem: <Homework 6 on strings. Finding new ways to work with strings.>

Certification of Authenticity:

I certify that this assignment is entirely my own work.

"""


def cash_converter():
    cash = eval(input("enter an integer: "))
    final = "That is ${}.00"
    print(final.format(cash))


def encode():
    s = input("Enter text: ")
    k = int(input("Enter key: "))

    e = "".join(chr(ord(c) + k) for c in s)

    print(e)



def sphere_area(radius):
    print("The area of the circle with radius " + str(radius) + " is: " + str(pi * radius**2))


def sphere_volume(radius):

    print("The volume of the circle with radius " + str(radius) +
          " is: " + str((4 / 3) * pi * radius * radius * radius))


def sum_n(number):
    sum1 = 0
    while (number > 0):
        sum1 = sum1 + number
        number = number - 1
    print("The sum of first n natural numbers is", sum1)


def sum_n_cubes(number):
    sum = 0
    for i in range(1, number + 1):
        sum += i * i * i

    print("The sum of first n natural numbers cubed is", sum)


def encode_better():
    message = input("Enter a message: ")
    k = input("Enter letters: ")

    output = ""
    for i in range(len(message)):
        shift = ord(message[i]) - 65
        val = ord(k[i % len(k)]) - 65
        val_end = (shift + val) % 58
        new = chr(val_end + 65)
        output = output + new
    print(output)




if __name__ == '__main__':
    # cash_converter()
    # encode()
    # res = sphere_area(13)
    # print(res)
    # res = sphere_volume(13)
    # print(res)
    # res = sum_n(100)
    # print(res)
    # res = sum_n_cubes(13)
    # print(res)
    # encode_better()
    pass
