def month_cost(x):
    #first 50 units will take Rs 15
    if x <= 50:
        cost = x * 15
    #second 50 units will take Rs 20
    elif x <= 100:
        cost = (50 * 15) + ((x - 50) * 20)
    #after the 100 units will take Rs 25
    else:
        cost = (50 * 35) + ((x - 100) * 25)
    return cost


def calculate ():
    name = input("Enter the Name with initial : ")
    address = input("Enter the address : ")
    first_read = int(input("Enter the unit last month read "))
    last_month_cost = float(input("Enter the last month bill Rs. "))
    last_month_pay = float(input("Enter the bill payment as you pay in last month Rs : "))
    second_read = int(input("Enter the unit current month read : "))

    total_unit = second_read - first_read
    arrias = last_month_cost - last_month_pay

    full_bill = arrias + month_cost(total_unit)

    print("Dear Customer, ")
    print("Your current bill is :")
    print(full_bill) 
    print(" ")
    print("Thank You ! ")

calculate()