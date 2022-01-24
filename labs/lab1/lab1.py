def net_balance():
    # step 1
    netbal = eval(input("Enter the Net Balance: "))
    days = eval(input("Enter the number of days in the billing cycle: "))
    balance1 = netbal * days


    # step 2
    netpay = eval(input("Enter the Payment received: "))
    remday = eval(input("Enter the number of days remaining in billing cycle: "))
    balance2 = netpay * remday


    # step 3

    balance3 = balance1 - balance2


    # step 4

    balance4 = balance3/days


    # step 5

    annualrate = eval(input("Enter the Annual Percentage Rate(as a decimal): "))
    monthlyrate = annualrate/12


    # step 6

    interestcharge = balance4 * monthlyrate
    print("Monthly Interest Charge(in dollars): ", interestcharge)


net_balance()
