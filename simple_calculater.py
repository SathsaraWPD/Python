def adding (x, y):
    sumi = x + y
    print('x + y =',sumi)

def substract (x, y):
    mini = x - y
    print('x - y',mini)

def multiple (x, y):
    multi = x * y 
    print('x * y',multi)

def divide (x, y):
    divi = x / y
    print('x / y',divi)

def calculate():
    
    print('1 - addition  2 - substraction  3 - multipication  4 - division')
    print(" ")

    num = int(input("Enter the number between 1 to 4 what do you want : "))
    if num >= 1 and num <= 4:
        num1 = int(input("Enter the first number : "))
        num2 = int(input("Enter the second number : "))
        print(" ")

        if num == 1:
            adding(num1, num2)
        elif num == 2:
            substract(num1, num2)
        elif num == 3:
            multiple(num1, num2)
        elif num == 4:
            divide(num1, num2)
    else:
        print("your input number is invalid...please input the number between 1 to 4") 


calculate()       