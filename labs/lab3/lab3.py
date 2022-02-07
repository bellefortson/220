"""
Name: <Belle Fortson>
<lab3>.py

Problem: <This assignment solves transportation problems>

Certification of Authenticity:

I certify that this assignment is entirely my own work.

"""

def transport():
    road = eval(input("How many roads were surveyed? "))
    total_acc = 0
    for i in range(1, road + 1):
        road_acc = 0
        print("How many days was road", i, "surveyed? ")
        days = eval(input(""))
        for j in range(1, days + 1):
            print("How many cars traveled on day", j, "? ")
            car = eval(input(""))
            road_acc = road_acc + car
        avg1 = road_acc / days
        print("Road", i, "average per day: ", avg1)
        total_acc = total_acc + road_acc
    total_avg = total_acc / road
    print("Total number of vehicles on all roads: ", total_acc)
    print("Average number of vehicles per road", total_avg)



transport()


